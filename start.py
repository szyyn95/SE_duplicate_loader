import argparse
from stackexchange_analyzer import Analyzer
import stackexchange_analyzer.util as util
import sys

# parser = argparse.ArgumentParser(description = 'Analyze data from StackExchange')
# parser.add_argument('--posts', type = str, default = './Posts.xml',
#                     help = 'XML posts dump from StackExchange')
# parser.add_argument('--postsLinks', type = str, default = './PostLinks.xml',
#                     help = 'XML posts links dump from StackExchange')
# parser.add_argument('--nonDuplicatesRatio', type = util.restricted_float, default = 1.5,
#                     help = 'Ratio of non-duplicate pairs versus duplicate raw pairs')
# parser.add_argument('--exportDirectory', type = str, default = '.',
# 					help='Directory for export file')
# parser.add_argument('--exportType', type = str, default = 'csv',
#                     help = 'Export file type (json/csv/txt)')
# parser.add_argument('--txtDelimiter', type = str, default = '||',
#                     help = 'Delimiter used for txt output')
# parser.add_argument('--mute', type = int, default = 1,
#                     help = 'Mute mode. 1 for true, 0 for false')
# args = parser.parse_args()

# analyzer = Analyzer(posts_path = args.posts,
#                     posts_links_path = args.postsLinks,
#                     ratio = args.nonDuplicatesRatio,
#                     mute = args.mute)

# analyzer.load_data()
# analyzer.analyze()
# analyzer.export(args.exportType, args.exportDirectory + "/result." + args.exportType, args.txtDelimiter)

def main(post, postlink, nonDuplicatesRation, exportDirectory, exportType, exportName, mute, delimiter):
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


     args = parser.parse_args()
     analyzer = Analyzer(posts_path = args.posts,
                         posts_links_path = args.postsLinks,
                         ratio = args.nonDuplicatesRatio,
                         mute = args.mute)

     analyzer.load_data()
     analyzer.analyze()
     # analyzer.export(args.exportType, args.exportDirectory + "/result_2." + args.exportType)
     analyzer.export(args.exportType, args.exportDirectory + exportName + "." + args.exportType, args.txtDelimiter)

if __name__ == '__main__':
     # in form of [location of Posts.xml, location of PostLinks.xml, nonDuplicatesRatio, exportDirectory, exportType, exportName]
     print(sys.argv)
     post = sys.argv[2]
     postlink = sys.argv[4]
     nonDuplicatesRation = sys.argv[6]
     exportDirectory = sys.argv[8]
     exportType = sys.argv[10]
     exportName = sys.argv[12]
     mute = sys.argv[14]
     delimiter = sys.argv[16]
     print(post)
     print(postlink)
     print(nonDuplicatesRation)
     print(exportDirectory)
     print(exportType)
     print(exportName)
     print(mute)
     print(delimiter)
     main(post, postlink, nonDuplicatesRation, exportDirectory, exportType, exportName, mute, delimiter)


