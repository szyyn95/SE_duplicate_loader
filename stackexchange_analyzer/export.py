import json
import csv

def export_to_json(res, export_path, delimiter):
	"""
	Not yet implemented
	"""
	print ("------NOT YET IMPLEMENTED------")
	return

def export_to_csv(res, export_path, delimiter):
	with open(export_path, 'w', newline='') as csvfile:
		fieldnames = ['idx', 'q1', 'q2', 'duplicate']
		writer = csv.DictWriter(csvfile, fieldnames = fieldnames)

		writer.writeheader()
		for curdict in res:
			writer.writerow(curdict)

def export_to_txt(res, export_path, delimiter):
	with open(export_path, 'w') as txtfile:
		txtfile.write(delimiter.join(['idx', 'q1', 'q2', 'duplicate']) + '\n')
		for curdict in res:
			txtfile.write(delimiter.join([str(curdict['idx']), curdict['q1'], curdict['q2'], curdict['duplicate']]) + '\n')
