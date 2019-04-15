import collections
import argparse
import csv

def restricted_float(x):
	x = float(x)
	if x <= 0.0:
		raise argparse.ArgumentTypeError("%r can't be non-positive"%(x,))
	return x

parser = argparse.ArgumentParser(description = 'Mixing StackExchange and Quora questions pairs with given ratio')

parser.add_argument('--SE_Path', type = str, default = 'SE_result/dev.tsv',
                    help = 'Path of StackExchange pairs, tsv format required.')
parser.add_argument('--QQP_Path', type = str, default = 'QQP/dev.tsv',
                    help = 'Path of Quora pairs, tsv format required.')
parser.add_argument('--Out_Path', type = str, default = 'Mixed/dev.tsv',
					help = 'Path of output file, tsv format required.')
parser.add_argument('--SE_amount', type = int, default = 100000,
					help = 'Number of StackExchange pairs. If the number available is less than this amount, use the maximum available number')
parser.add_argument('--ratio', type = restricted_float, default = 1.0,
					help = 'Ratio of SE pairs and Quora pairs. The float n defined here means n Quora pairs for every SE pair. Again, we use the maximum available ratio if no enough Quora pairs.')

args = parser.parse_args()
SE_read, QQP_read = 0, 0 # number of SE/QQP pairs we've read
acc_pair = 0

with open(args.SE_Path, 'r') as SE_file, open(args.Out_Path, 'w') as out_file:
	SE_reader = csv.reader(SE_file, delimiter = '\t')
	writer = csv.writer(out_file, delimiter = '\t')
	next(SE_reader, None) # skip header
	writer.writerow(['id', 'qid1', 'qid2', 'question1', 'question2', 'is_duplicate']) #write header in out file
	for row in SE_reader:
		row[0] = acc_pair
		# add header notation to SE pair qids
		row[1] = 'SE-' + row[1]
		row[2] = 'SE-' + row[2]
		writer.writerow(row)

		acc_pair += 1
		SE_read += 1
		if SE_read == args.SE_amount:
			break

	SE_file.close()
	out_file.close()

QQP_num = int(round(min(args.SE_amount, SE_read) * args.ratio))

with open(args.QQP_Path, 'r') as QQP_file, open(args.Out_Path, 'a') as out_file:
	QQP_reader = csv.reader(QQP_file, delimiter = '\t')
	writer = csv.writer(out_file, delimiter = '\t')
	next(QQP_reader, None) # skip header
	for row in QQP_reader:
		row[0] = acc_pair
		# add header notation to QQP pair qids
		row[1] = 'QQP-' + row[1]
		row[2] = 'QQP-' + row[2]
		writer.writerow(row)

		acc_pair += 1
		QQP_read += 1
		if QQP_read == QQP_num:
			break

	QQP_file.close()
	out_file.close()

print ('Num of SE pairs mixed: ' + str(min(args.SE_amount, SE_read)))
print ('Num of QQP pairs mixed: ' + str(min(QQP_num, QQP_read)))
