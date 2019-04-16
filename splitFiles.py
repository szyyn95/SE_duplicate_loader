import csv
from random import shuffle
import os
cwd = os.getcwd()

train_ration = 0.8
dev_ration = 0.1

for file in os.listdir(cwd + "/unsplitted_mixed_intermediate_set"):
	
	newname = file[:-4]

	reader = csv.reader(open(cwd + "/unsplitted_mixed_intermediate_set/" + file, 'r'), delimiter="\t")
	lines = list(reader)
	shuffle(lines)
	print(len(lines))

	train_bottom_line = int(train_ration * len(lines))
	dev_bottom_line = int((train_ration + dev_ration) * len(lines))
	train = lines[ : train_bottom_line]
	dev = lines[train_bottom_line: dev_bottom_line]
	test_tmp = lines[dev_bottom_line:]
	test = list()
	for t in test_tmp:
		test.append([t[0],t[3], t[4]])

	os.makedirs(os.path.dirname(cwd + "/" + newname + "/test.tsv"), exist_ok=True)
	with open(cwd + "/" + newname + "/test.tsv", 'w') as csvfile:
		fieldnames = ["id","question1","question2"]
		w = csv.writer(csvfile, delimiter='\t')
		w.writerow(fieldnames)
		w.writerows(test)

	os.makedirs(os.path.dirname(cwd + "/" + newname + "/train.tsv"), exist_ok=True)
	with open(cwd + "/" + newname + "/train.tsv", 'w') as csvfile:
		fieldnames = ["id","qid1","qid2","question1","question2","is_duplicate"]
		w = csv.writer(csvfile, delimiter='\t')
		w.writerow(fieldnames)
		w.writerows(train)

	os.makedirs(os.path.dirname(cwd + "/" + newname + "/dev.tsv"), exist_ok=True)
	with open(cwd + "/" + newname + "/dev.tsv", 'w') as csvfile:
		fieldnames = ["id","qid1","qid2","question1","question2","is_duplicate"]
		w = csv.writer(csvfile, delimiter='\t')
		w.writerow(fieldnames)
		w.writerows(dev)
