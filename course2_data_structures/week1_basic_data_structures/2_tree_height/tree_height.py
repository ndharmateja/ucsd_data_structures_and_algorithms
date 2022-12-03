# python3

import sys
import threading


class Node:
    def __init__(self) -> None:
        self.children = []


def height(node: Node):
    if len(node.children) == 0:
        return 1

    max_child_height = 0
    for child in node.children:
        max_child_height = max(max_child_height, height(child))

    return 1 + max_child_height


def compute_height(n, parents: list):
    nodes = [Node() for _ in parents]

    for i, parent in enumerate(parents):
        if parent != -1:
            node = nodes[i]
            parent_node = nodes[parent]
            parent_node.children.append(node)

    root = nodes[parents.index(-1)]

    return height(root)


def main():
    n = int(input())
    parents = list(map(int, input().split()))
    print(compute_height(n, parents))


# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()
