import xml.etree.ElementTree as ElementTree
import stackexchange_analyzer.export as export

EXPORT_TYPES = {'json': export.export_to_json, 'html': export.export_to_html}


class Analyzer:
    """Class that loads from file and analyze StackExchange data"""
    def __init__(self, posts_path, posts_links_path, posts_num):
        # Posts dump file path
        self.posts_path = posts_path
        # ElementTree root for posts
        self.posts = None

        # Posts links dump file path
        self.posts_links_path = posts_links_path
        # ElementTree root for posts links
        self.posts_links = None

        # Most duplicated posts.
        # [(post_id, [duplicate_id, ...]), ...]
        self.top_duplicated_posts = None

        # Num of top duplicated posts to show
        self.posts_num = posts_num

        # Information about most duplicated posts. List of summaries.
        # [{title: 'Some question', link: '...', duplicates_num: 10,
        #   duplicates: [{title: '...', link: '...'}, ...]}]
        self.result = []

    def load_data(self):
        """Load dump files to memory"""
        print('Loading data...')
        self.posts = ElementTree.parse(self.posts_path).getroot()
        self.posts_links = ElementTree.parse(self.posts_links_path).getroot()
        print('Data loaded.')

    def analyze(self):
        """Analyze dumps and prepare data to export"""
        print('Analyze started.')
        self._find_top_duplicates(self.posts_num)
        self._prepare_result()

    def _find_top_duplicates(self, n=100):
        print('Counting posts duplicates...')
        # There is a problem in Stackoverflow dataset.
        # If question was deleted by moderator, all relations with it don't
        # deleting too. So we should manually check is post deleted or not.
        all_posts_ids = set()
        for post in self.posts:
            post = dict(post.items())
            all_posts_ids.add(post['Id'])

        post_duplicates = {}
        for post_link in self.posts_links:
            # Convert entry to a dict
            post_link = dict(post_link.items())
            # If not 'duplicate' relation, just pass it
            if not post_link['LinkTypeId'] == '3':
                continue
            post_id = post_link['PostId']
            related_post = post_link['RelatedPostId']
            # If one of posts is deleted, pass it too
            if (post_id not in all_posts_ids
                or related_post not in all_posts_ids):
                continue
            # Add new duplicate to duplicates list
            current_duplicates = post_duplicates.get(post_id, [])
            post_duplicates[related_post] = current_duplicates + [post_id]
        print('Duplicates counted.')
        print('Sorting duplicates...')
        # Get only n (by default, 100) first elements
        self.top_duplicated_posts = sorted(post_duplicates.items(),
                                           key=lambda x: len(x[1]),
                                           reverse=True)[:n]
        print('Duplication top:', self.top_duplicated_posts)
        print('Sorting done.')

    def _prepare_result(self):
        """Load information about posts and duplicates
           to prepare information for exporting result"""
        # All posts are storing in the list with len == n.
        # So if we will load information about each post in duplicates top,
        # algorithm will work for O((k * m) * n), where k is self.posts_num and
        # m is average of numbers of duplicates from question duplication top.
        # Optimization. Let's save all needed posts ids to set and iterate
        # throw all posts list only one time.
        # It will work for O(k * m + n + (k * m)^2). Because k and m much
        # smaller than n, it will be work faster.
        result_posts_ids = set()
        for post in self.top_duplicated_posts:
            result_posts_ids.add(post[0])
            for duplicate in post[1]:
                result_posts_ids.add(duplicate)

        result_posts_data = []
        for post in self.posts:
            post = dict(post.items())
            if post['Id'] in result_posts_ids:
                result_posts_data.append(post)

        for result_post in self.top_duplicated_posts:
            post_summary = {}
            for post in result_posts_data:
                if post['Id'] == result_post[0]:
                    post_summary['title'] = post['Title']
                    break
            duplicates_summaries = []
            for duplicate_id in result_post[1]:
                for post in result_posts_data:
                    if post['Id'] == duplicate_id:
                        duplicate_summary = {}
                        duplicate_summary['title'] = post['Title']
                        duplicates_summaries.append(duplicate_summary)
            post_summary['duplicates'] = duplicates_summaries
            self.result.append(post_summary)

    def export(self, export_type, export_file):
        """Export result using one of exporters in export.py"""
        print('Exporting to', export_type)
        # Run export function
        EXPORT_TYPES[export_type](self.result, export_file)
        print('Export done.')
