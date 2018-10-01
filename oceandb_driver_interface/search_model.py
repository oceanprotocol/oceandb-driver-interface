from collections import namedtuple

sort = namedtuple('key', 'direction')


class QueryModel(object):
    def __init__(self, query=None, sorting: [list[sort]] = None, offset=100, page=0):
        self.query = query
        self.sort = sorting
        self.offset = offset
        self.page = page


class FullTextModel(object):
    def __init__(self, text=None, sorting: [list[sort]] = None, offset=100, page=0):
        self.text = text
        self.sort = sorting
        self.offset = offset
        self.page = page
