import argparse
from stackexchange_analyzer import Analyzer
import stackexchange_analyzer.util as util
import sys

parser = argparse.ArgumentParser(description = 'Analyze data from StackExchange')

parser.add_argument('--posts', type = str, default = post,
						help = 'XML posts dump from StackExchange')
parser.add_argument('--postsLinks', type = str, default = postlink,
					help = 'XML posts links dump from StackExchange')
parser.add_argument('--nonDuplicatesRatio', type = util.restricted_float, default = 1.5,
					help = 'Ratio of non-duplicate pairs versus duplicate raw pairs')
parser.add_argument('--exportDirectory', type = str, default = exportDirectory,
	 					help='Directory for export file')
parser.add_argument('--exportType', type = str, default = exportType,
						help = 'Export file type (json/csv/txt)')
parser.add_argument('--txtDelimiter', type = str, default = '||',
						help = 'Delimiter used for txt output')
parser.add_argument('--mute', type = int, default = 1,
						help = 'Mute mode. 1 for true, 0 for false')
parser.add_argument('--exportName', type = str, default = exportName,
					help = 'Export file name')

args = parser.parse_args()
analyzer = Analyzer(posts_path = args.posts,
					posts_links_path = args.postsLinks,
					ratio = args.nonDuplicatesRatio,
					mute = args.mute)
analyzer.load_data()
analyzer.analyze()
analyzer.export(args.exportType, args.exportDirectory + args.exportName + "." + args.exportType, args.txtDelimiter)


