#!/usr/bin/python3

import sys
import threading

sys.setrecursionlimit(10**8)  # max depth of recursion
threading.stack_size(2**26)  # new thread will get stack of such size


def is_bst(tree):
    if len(tree) == 0:
        return True

    two_31 = 2 ** 31
    return is_bst_helper(tree, 0, -two_31, two_31 - 1)


def is_bst_helper(tree, index, min, max):
    if index == -1:
        return True

    [key, left_index, right_index] = tree[index]
    if key < min or key > max:
        return False

    return is_bst_helper(tree, left_index, min, key - 1) and is_bst_helper(tree, right_index, key + 1, max)


def main():
    nodes = int(sys.stdin.readline().strip())
    tree = []
    for i in range(nodes):
        tree.append(list(map(int, sys.stdin.readline().strip().split())))
    # tree = [
    #     [4, 1, -1],
    #     [2, 2, 3],
    #     [1, -1, -1],
    #     [5, -1, -1]
    # ]
    if is_bst(tree):
        print("CORRECT")
    else:
        print("INCORRECT")


threading.Thread(target=main).start()
