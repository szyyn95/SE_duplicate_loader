import argparse
import csv

parser = argparse.ArgumentParser(description = 'General spliter to split data sets with certain ratio')

parser.add_argument('--input_path', type = str, default = './SE_result/full_train.tsv',
                    help = 'Path of input files, tsv format required.')
parser.add_argument('--output_path1', type = str, default = './SE_result/intermediate_train.tsv',
                    help = 'Path of the first output files, tsv format required.')
parser.add_argument('--output_path2', type = str, default = './SE_result/train.tsv',
                    help = 'Path of the second output files, tsv format required.')
parser.add_argument('--amount', type = int, default = 200000,
                    help = 'Sepcify the amount of data for first output. The rest will be in the second')

args = parser.parse_args()
acc_pair = 0
header = None

with open(args.input_path, 'r') as input_file, open(args.output_path1, 'w') as out_file1, open(args.output_path2, 'w') as out_file2:
	reader = csv.reader(input_file, delimiter = '\t')
	writer1 = csv.writer(out_file1, delimiter = '\t')
	writer2 = csv.writer(out_file2, delimiter = '\t')
	header = next(reader, None)
	writer1.writerow(header)
	writer2.writerow(header)

	for row in reader:
		if acc_pair < args.amount:
			writer1.writerow(row)
		else:
			writer2.writerow(row)
		acc_pair += 1

input_file.close()
out_file1.close()
out_file2.close()