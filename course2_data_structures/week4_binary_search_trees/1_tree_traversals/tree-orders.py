# python3

import sys
import threading
sys.setrecursionlimit(10**6)  # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size


class TreeOrders:
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

    def inorder(self):
        self.inorder_result = []
        self.inorder_helper(0)
        return self.inorder_result

    def inorder_helper(self, index):
        if index == -1:
            return
        self.inorder_helper(self.left[index])
        self.inorder_result.append(self.key[index])
        self.inorder_helper(self.right[index])

    def preorder(self):
        self.preorder_result = []
        self.preorder_helper(0)
        return self.preorder_result

    def preorder_helper(self, index):
        if index == -1:
            return
        self.preorder_result.append(self.key[index])
        self.preorder_helper(self.left[index])
        self.preorder_helper(self.right[index])

    def postorder(self):
        self.postorder_result = []
        self.postorder_helper(0)
        return self.postorder_result

    def postorder_helper(self, index):
        if index == -1:
            return
        self.postorder_helper(self.left[index])
        self.postorder_helper(self.right[index])
        self.postorder_result.append(self.key[index])


def main():
    tree = TreeOrders()
    tree.read()
    print(" ".join(str(x) for x in tree.inorder()))
    print(" ".join(str(x) for x in tree.preorder()))
    print(" ".join(str(x) for x in tree.postorder()))


threading.Thread(target=main).start()
