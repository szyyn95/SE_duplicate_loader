import pandas as pd

df = pd.read_csv('Target5k_val.tsv', sep = '\t')

def rm_hashtab(s):
	if type(s) is str:
		return s.replace(' ##', '')
	return s

def rm_quote(s):
	if type(s) is str:
		return s.replace('" "', '')
	return s

df = df.applymap(rm_hashtab)
df = df.applymap(rm_quote)

# add manual tag column
if 'manual_label' not in list(df.columns.values):
	df['manual_label'] = ''

df.to_csv('Target5k_definite.tsv', sep = '\t')