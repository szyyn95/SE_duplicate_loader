import collections
import argparse

def parse_body(body):
	"""
	DEPRECATED

	Body follows HTML format, each question/comment are surrounded by indicators like <p><p/>, <h1><h1/>, etc.
	"""
	question_block_indicator = "p"
	if body[4] == "h":
		# if <h1>, <h2>...
		question_block_indicator = body[4:6]
	question_block_start = "<" + question_block_indicator + ">"
	question_block_end = "</" + question_block_indicator + ">"
	question_body = body.split(question_block_end)[0]
	#question_body = question_body.split(question_block_start)[1]
	return question_body

def restricted_float(x):
	x = float(x)
	if x <= 0.0:
		raise argparse.ArgumentTypeError("%r can't be non-positive"%(x,))
	return x