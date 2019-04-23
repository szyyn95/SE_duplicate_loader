import collections
import argparse
import csv

"""
Total number of mixed pairs is fixed to make sure that all intermediate tasks have fixed amount of data
"""

def restricted_float(x):
	x = float(x)
	if x < 0.0 or x > 1.0:
		raise argparse.ArgumentTypeError("%r is not a valid ratio"%(x,))
	return x

parser = argparse.ArgumentParser(description = 'Mixing StackExchange and Quora questions pairs with given ratio')

parser.add_argument('--SE_path', type = str, default = './SE_result/train.tsv',
                    help = 'Path of StackExchange pairs, tsv format required.')
parser.add_argument('--QQP_path', type = str, default = './QQP/train.tsv',
                    help = 'Path of Quora pairs, tsv format required.')
parser.add_argument('--Out_path', type = str, default = './Mixed/Mixed',
					help = 'Path of output file, tsv format required.')
parser.add_argument('--total_amount', type = int, default = 200000,
					help = 'Total number of pairs in the mixed data set. The input here should not exceed 20000.')
parser.add_argument('--ratio', type = restricted_float, default = 0.5,
					help = 'Ratio of SE pairs within the whole mixed set. Valid input from 0.0 to 1.0.')

args = parser.parse_args()
args.Out_path = args.Out_path + '_' + str(int(args.ratio * 10)) + '.tsv'
SE_read, QQP_read = 0, 0 # number of SE/QQP pairs we've read
acc_pair = 0

SE_num = int(round(args.total_amount * args.ratio))
QQP_num = args.total_amount - SE_num

with open(args.SE_path, 'r') as SE_file, open(args.Out_path, 'w') as out_file:
	SE_reader = csv.reader(SE_file, delimiter = '\t')
	mixed_writer = csv.writer(out_file, delimiter = '\t')

	next(SE_reader, None) # skip header
	mixed_writer.writerow(['id', 'qid1', 'qid2', 'question1', 'question2', 'is_duplicate']) #write header in out file

	for row in SE_reader:
		if SE_read >= SE_num:
			break
		try:	
			row[0] = acc_pair
			# add header notation to SE pair qids
			row[1] = 'SE-' + row[1]
			row[2] = 'SE-' + row[2]
			mixed_writer.writerow(row)

			acc_pair += 1
			SE_read += 1
		except:
			continue

	SE_file.close()
	out_file.close()

with open(args.QQP_path, 'r') as QQP_file, open(args.Out_path, 'a') as out_file:
	QQP_reader = csv.reader(QQP_file, delimiter = '\t')
	mixed_writer = csv.writer(out_file, delimiter = '\t')
	next(QQP_reader, None) # skip header
	for row in QQP_reader:
		if QQP_read >= QQP_num:
			break
		try:
			row[0] = acc_pair
			# add header notation to QQP pair qids
			row[1] = 'QQP-' + row[1]
			row[2] = 'QQP-' + row[2]
			mixed_writer.writerow(row)

			acc_pair += 1
			QQP_read += 1
		except:
			continue

	QQP_file.close()
	out_file.close()

print ('Num of SE pairs mixed: ' + str(SE_num))
print ('Num of QQP pairs mixed: ' + str(QQP_num))

if SE_num > SE_read:
	print ('Warning: no enough SE pairs.')
if QQP_num > QQP_read:
	print ('Warning: no enough QQP pairs.')
