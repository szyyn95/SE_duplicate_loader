import xml.etree.ElementTree as ElementTree
import stackexchange_analyzer.export as export
import stackexchange_analyzer.util as util
import random
import collections

EXPORT_TYPES = {'json': export.export_to_json, 
                'csv': export.export_to_csv}


class Analyzer:
    """Class that loads from file and analyze StackExchange data"""
    def __init__(self, posts_path, posts_links_path, ratio):
        self.posts_path = posts_path
        self.posts = {} # here we only record all questions (which contains 'Title' field)
        self.posts_links_path = posts_links_path
        self.posts_links = None
        self.all_posts_ids = set()
        self.duplicated_posts = {}
        self.nonduplicated_posts = []

        self.ratio = ratio
        self.dups = 0
        self.res = []

    def load_data(self):
        """Load dump files to memory"""
        print('Loading data...')
        raw_posts = ElementTree.parse(self.posts_path).getroot()
        for raw_post in raw_posts:
            raw_post = dict(raw_post.items())
            if 'Title' in raw_post:
                # we only keep questions 
                self.posts[raw_post['Id']] = raw_post['Title']

        self.posts_links = ElementTree.parse(self.posts_links_path).getroot()
        print('Data loaded.')

    def analyze(self):
        """Analyze dumps and prepare data to export"""
        print('Analyze started.')
        self._find_top_duplicates()
        self._generate_noneDuplicates()
        self.duplicated_posts = self.duplicated_posts.items()
        self._prepare_result()

    def _find_top_duplicates(self):
        print('Counting posts duplicates...')
        # There is a problem in Stackoverflow dataset.
        # If question was deleted by moderator, all relations with it don't
        # deleting too. So we should manually check is post deleted or not.
        for post_link in self.posts_links:
            # Convert entry to a dict
            post_link = dict(post_link.items())
            # If not 'duplicate' relation, just pass it
            if post_link['LinkTypeId'] != '3':
                continue
            post_id = post_link['PostId']
            related_post = post_link['RelatedPostId']
            # If one of posts is deleted, pass it too
            if (post_id not in self.posts or related_post not in self.posts):
                continue
            # Add new duplicate to duplicates list
            cur_dups = self.duplicated_posts.get(post_id, [])
            self.duplicated_posts[related_post] = cur_dups + [post_id]

        for dup in self.duplicated_posts:
            self.dups += len(self.duplicated_posts[dup])
        print (self.duplicated_posts)
        return

    def _generate_noneDuplicates(self):
        nondup_amount = int(round(self.dups * self.ratio))
        print ("Non-duplicate pairs amount: " + str(nondup_amount))
        used_pair = collections.defaultdict(set)
        while True:
            id1, id2 = random.sample(self.posts.keys(), 2)
            if id1 in self.duplicated_posts.get(id2, []) or id2 in self.duplicated_posts.get(id1, []):
                continue
            if id1 in used_pair[id2] or id2 in used_pair[id1]:
                continue
            self.nonduplicated_posts.append([id1, id2])
            used_pair[id2].add(id1)
            used_pair[id1].add(id2)
            if len(self.nonduplicated_posts) >= nondup_amount:
                break

        print (self.nonduplicated_posts)
        return

    def _prepare_result(self):
        for id1, id2 in self.nonduplicated_posts:
            newdict = {}
            newdict['q1'] = self.posts[id1]
            newdict['q2'] = self.posts[id2]
            newdict['duplicate'] = '0'
            self.res.append(newdict)
        for idl, idrs in self.duplicated_posts:
            for idr in idrs:
                newdict = {}
                newdict['q1'] = self.posts[idl]
                newdict['q2'] = self.posts[idr]
                newdict['duplicate'] = '1'
                self.res.append(newdict)
        random.shuffle(self.res)

        cur_idx = 1
        for cur_dict in self.res:
            cur_dict['idx'] = cur_idx
            cur_idx += 1
        print (self.res)

    def export(self, export_type, export_file):
        """Export result using one of exporters in export.py"""
        print('Exporting to', export_type)
        # Run export function
        EXPORT_TYPES[export_type](self.res, export_file)
        print('Export done.')
