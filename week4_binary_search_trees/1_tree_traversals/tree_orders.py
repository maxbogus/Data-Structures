# python3

import sys
import threading

sys.setrecursionlimit(10 ** 6)  # max depth of recursion
threading.stack_size(2 ** 27)  # new thread will get stack of such size


class TreeOrders:
    def __init__(self, key=None, left=None, right=None, n=0):
        if key is None:
            key = []
        if left is None:
            left = []
        if right is None:
            right = []
        self.n = n  # vertices
        self.key = key  # key
        self.left = left  # left
        self.right = right  # right
        self.result = {
            'in_order': [],
            'post_order': [],
            'pre_order': []
        }

    def read(self):
        self.n = int(sys.stdin.readline())
        self.key = [0 for i in range(self.n)]
        self.left = [0 for i in range(self.n)]
        self.right = [0 for i in range(self.n)]
        for i in range(self.n):
            [a, b, c] = map(int, sys.stdin.readline().split())
            self.key[i] = a
            self.left[i] = b
            self.right[i] = c

    def read_from_array(self, n, data):
        self.n = n
        self.key = [0 for i in range(self.n)]
        self.left = [0 for i in range(self.n)]
        self.right = [0 for i in range(self.n)]
        for i in range(self.n):
            [a, b, c] = data[i]
            self.key[i] = a
            self.left[i] = b
            self.right[i] = c

    def in_order(self, key=None):
        # Finish the implementation
        # You may need to add a new recursive method to do that
        if not self.key or key == -1:
            return

        if key is None:
            key = 0

        self.in_order(self.left[key])
        self.result['in_order'].append(self.key[key])
        self.in_order(self.right[key])

        return self.result['in_order']

    def pre_order(self, key=None):
        # Finish the implementation
        # You may need to add a new recursive method to do that
        if not self.key or key == -1:
            return

        if key is None:
            key = 0

        self.result['pre_order'].append(self.key[key])
        self.pre_order(self.left[key])
        self.pre_order(self.right[key])

        return self.result['pre_order']

    def post_order(self, key=None):
        # Finish the implementation
        # You may need to add a new recursive method to do that
        if not self.key or key == -1:
            return

        if key is None:
            key = 0

        self.post_order(self.left[key])
        self.post_order(self.right[key])
        self.result['post_order'].append(self.key[key])

        return self.result['post_order']


def main():
    tree = TreeOrders()
    tree.read()
    print(" ".join(str(x) for x in tree.in_order()))
    print(" ".join(str(x) for x in tree.pre_order()))
    print(" ".join(str(x) for x in tree.post_order()))


threading.Thread(target=main).start()
