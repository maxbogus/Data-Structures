# python3

import sys
import threading

sys.setrecursionlimit(10 ** 7)  # max depth of recursion
threading.stack_size(2 ** 27)  # new thread will get stack of such size


class TreeHeight:
    def __init__(self, arr, n):
        self.parent = arr
        self.n = n

    def read(self):
        print(self.parent, self.n)

    def compute_height(self):
        # Replace this code with a faster implementation
        max_height = 0
        for vertex in range(self.n):
            height = 0
            i = vertex
            while i != -1:
                height += 1
                i = self.parent[i]
            max_height = max(max_height, height)
        return max_height


    def compute_height_fast(self):
        nodes = [0] * self.n
        for i in self.arr:
            nodes[i]
        return 0


def main():
    tree = TreeHeight([4, -1, 4, 1, 1], 5)
    tree.read()
    print(tree.compute_height())


threading.Thread(target=main).start()
