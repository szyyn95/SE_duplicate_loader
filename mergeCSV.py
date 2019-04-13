import csv
import os

import os
cwd = os.getcwd()

selectedFiles = cwd + "/sorted.txt"
directory = cwd + "/allTXT/"
deduplicate = dict()
index = 0
question_pair = 1
export_path = cwd + "/out.csv"

count = 0
with open(export_path, 'a', newline='') as csvfile:
	for line in open(selectedFiles):
		filename = line.split("./")[1][:-1]
		print(filename)
		fieldnames = ["id","qid1","qid2","question1","question2","is_duplicate"]
		writer = csv.DictWriter(csvfile, fieldnames = fieldnames)
		writer.writeheader()

		# for filename in os.listdir(directory):
		for line in open(directory + filename):
			curdict = dict()
			line_array = line.split("<***>")
			if line_array[0] == "idx":
				continue
			curdict['id'] = question_pair
			question_pair += 1
			curdict['question1'] = line_array[1]
			curdict['question2'] = line_array[2]
			curdict['is_duplicate'] = line_array[3].split("\n")[0]
			if line_array[1] not in deduplicate:
				deduplicate[line_array[1]] = index
				curdict['qid1'] = index
				index +=1
			else:
				curdict['qid1'] = deduplicate[line_array[1]]

			if line_array[2] not in deduplicate:
				deduplicate[line_array[2]] = index
				curdict['qid2'] = index
				index +=1
			else:
				curdict['qid2'] = deduplicate[line_array[2]]

			writer.writerow(curdict)
		count += 1
		if count == 100:
			break

