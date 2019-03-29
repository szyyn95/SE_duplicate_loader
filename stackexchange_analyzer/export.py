import json
import csv

def export_to_json(res, export_path):
	return

def export_to_csv(res, export_path):
	with open(export_path, 'w', newline='') as csvfile:
		fieldnames = ['idx', 'q1', 'q2', 'duplicate']
		writer = csv.DictWriter(csvfile, fieldnames = fieldnames)

		writer.writeheader()
		for curdict in res:
			writer.writerow(curdict)
