from typing import Tuple, List

sort = Tuple[str, str]


class QueryModel(object):
    def __init__(self, query=None, sorting: List[sort] = None, offset=100, page=0):
        self.query = query
        self.sort = sorting
        self.offset = offset
        self.page = page


class FullTextModel():
    def __init__(self, text=None, sorting: List[sort] = None, offset=100, page=0):
        self.text = text
        self.sort = sorting
        self.offset = offset
        self.page = page
