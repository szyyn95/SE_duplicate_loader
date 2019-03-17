import argparse
from stackexchange_analyzer import Analyzer

parser = argparse.ArgumentParser(description = 'Analyze data from StackExchange')
parser.add_argument('--posts', type = str, default = './Posts.xml',
                    help = 'XML posts dump from StackExchange')
parser.add_argument('--postsLinks', type = str, default = './PostLinks.xml',
                    help = 'XML posts links dump from StackExchange')
parser.add_argument('--postsNum', type = int, default = 100,
                    help = 'Number of top duplicated posts to show')
parser.add_argument('--exportFile', type = str, default = './result.html',
                    help = 'Path for export file')
parser.add_argument('--exportType', type = str, default = 'html',
                    help = 'Export file type (json/html)')
args = parser.parse_args()

analyzer = Analyzer(posts_path = args.posts,
                    posts_links_path = args.postsLinks,
                    posts_num = args.postsNum)

analyzer.load_data()
analyzer.analyze()
analyzer.export(args.exportType, args.exportFile)
