#!/usr/bin/python3

import sys, threading
from math import inf

sys.setrecursionlimit(10 ** 7)  # max depth of recursion
threading.stack_size(2 ** 27)  # new thread will get stack of such size


def IsBinarySearchTree(tree):
    if not tree:
        return True
    left = []
    right = []
    key = []

    if len(tree) == 1 or len(tree) == 0:
        return True

    for item in tree:
        if len(item) == 3:
            [a, b, c] = item
            key.append(a)
            left.append(b)
            right.append(c)

    failures = []
    result = []

    def in_order(index, max_value, min_value):
        if not key or index == -1:
            return -1

        current_val = key[index]
        in_order(left[index], current_val - 1, min_value)
        if current_val > max_value or current_val < min_value:
            failures.append(False)
        result.append(current_val)
        in_order(right[index], max_value, current_val)

    in_order(0, inf, -inf)
    for item in failures:
        if not item:
            return False

    unsorted = result
    result.sort()
    return unsorted == result


def main():
    nodes = int(sys.stdin.readline().strip())
    tree = []
    for i in range(nodes):
        tree.append(list(map(int, sys.stdin.readline().strip().split())))
    if IsBinarySearchTree(tree):
        print("CORRECT")
    else:
        print("INCORRECT")


def main_with_args(n, data=None):
    if data is None:
        data = []
    tree = []
    if n > 0:
        for node in range(n):
            tree.append(data[node])
    if IsBinarySearchTree(tree):
        return "CORRECT"
    else:
        return "INCORRECT"


threading.Thread(target=main).start()
