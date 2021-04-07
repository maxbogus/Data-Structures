#!/usr/bin/python3

import sys
import threading

sys.setrecursionlimit(10 ** 7)  # max depth of recursion
threading.stack_size(2 ** 27)  # new thread will get stack of such size


def IsBinarySearchTree(tree):
    if not tree:
        return True

    left = []
    right = []
    key = []
    sorted_keys = []

    if len(tree) == 1 or len(tree) == 0:
        return True

    for item in tree:
        [a, b, c] = item
        key.append(a)
        left.append(b)
        right.append(c)

    def store_in_order(root_index, arr):
        if root_index == -1:
            return
        store_in_order(left[root_index], arr)
        arr.append(key[root_index])
        store_in_order(right[root_index], arr)

    store_in_order(0, sorted_keys)
    for i in range(1, len(sorted_keys)):
        if sorted_keys[i] < sorted_keys[i-1]:
            return False

    return True


def IsBinarySearchTree_naive(tree):
    if not tree:
        return True

    left = []
    right = []
    key = []
    result = True
    root = None

    if len(tree) == 1 or len(tree) == 0:
        return True

    for item in tree:
        [a, b, c] = item
        key.append(a)
        left.append(b)
        right.append(c)

    def in_order(root, key_index=None, traverse=None, parent_value=None, branch=None):
        if not key or key_index == -1:
            return

        if key_index is None:
            key_index = 0

        current_value = key[key_index]
        if traverse == "right":
            if current_value < parent_value:
                return "False"

        if traverse == "left":
            if current_value > parent_value:
                return "False"

        if branch == "left":
            if current_value > root:
                return "False"
        if branch == "right":
            if current_value < root:
                return "False"

        if in_order(root, left[key_index], "left", current_value, "left" if branch is None else branch) == "False":
            return "False"
        if in_order(root, right[key_index], "right", current_value, "right" if branch is None else branch) == "False":
            return "False"

    if key and len(key) > 0:
        root = key[0]

    if in_order(root, None, None, None, None) == "False":
        return False

    return result


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
    if IsBinarySearchTree_naive(tree):
        return "CORRECT"
    else:
        return "INCORRECT"


threading.Thread(target=main).start()
