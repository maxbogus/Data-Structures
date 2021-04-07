# python3

class Query:

    def __init__(self, query):
        self.type = query[0]
        if self.type == 'check':
            self.ind = int(query[1])
        else:
            self.s = query[1]


def write_chain(chain):
    print(' '.join(chain))


def write_search_result(was_found):
    print('yes' if was_found else 'no')


def read_querie_with_arg(data):
    return Query(data.split())


def read_query():
    return Query(input().split())


class QueryProcessor:
    _multiplier = 263
    _prime = 1000000007

    def __init__(self, buckets_count):
        self.bucket_count = buckets_count
        # store all strings in one list
        self.elements = []

    def _hash_func(self, s):
        ans = 0
        for c in reversed(s):
            ans = (ans * self._multiplier + ord(c)) % self._prime
        return ans % self.bucket_count

    def process_query(self, query):
        if query.type == "check":
            # use reverse order, because we append strings to the end
            write_chain(cur for cur in reversed(self.elements)
                        if self._hash_func(cur) == query.ind)
        else:
            try:
                ind = self.elements.index(query.s)
            except ValueError:
                ind = -1
            if query.type == 'find':
                write_search_result(ind != -1)
            elif query.type == 'add':
                if ind == -1:
                    self.elements.append(query.s)
            else:
                if ind != -1:
                    self.elements.pop(ind)

    def process_query_naive(self, query):
        if query.type == "check":
            # use reverse order, because we append strings to the end
            write_chain(cur for cur in reversed(self.elements)
                        if self._hash_func(cur) == query.ind)
        else:
            try:
                ind = self.elements.index(query.s)
            except ValueError:
                ind = -1
            if query.type == 'find':
                write_search_result(ind != -1)
            elif query.type == 'add':
                if ind == -1:
                    self.elements.append(query.s)
            else:
                if ind != -1:
                    self.elements.pop(ind)

    def process_queries(self):
        n = int(input())
        for i in range(n):
            self.process_query(read_query())

    def process_queries_arg(self, lst):
        for item in lst:
            self.process_query(read_querie_with_arg(item))


if __name__ == '__main__':
    bucket_count = int(input())
    proc = QueryProcessor(bucket_count)
    proc.process_queries()
