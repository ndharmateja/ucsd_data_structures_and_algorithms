# python3

import sys
import random


class Solver:
    def __init__(self, string):
        self.string = string
        self.n = len(self.string)

        # 0th index of self.hashes, self.p, self.x_l
        # contains values corresponding to the first hash
        # (we are doing two separate hashes to reduce probability)
        # Similary for 1st index
        self.hashes = [[0 for _ in range(self.n + 1)] for __ in range(2)]
        self.p = [10**9 + 7, 10**9 + 9]
        self.x = random.randint(0, 10**9)

        # 0th index contains the powers x^0, x^1 .. x^n with modulus p[0]
        # Similary for 1st index
        self.x_l = [[1 for _ in range(self.n + 1)] for __ in range(2)]

        # precompute hashes and powers
        self.precompute_prefix_hashes()

    def precompute_prefix_hashes(self):
        # loop over the characters of the string
        for i, char in enumerate(self.string, 1):
            # loop for 0th and 1st indexes
            for j in range(2):
                self.hashes[j][i] = (((self.x * self.hashes[j][i - 1]) %
                                      self.p[j]) + ord(char)) % self.p[j]
                self.x_l[j][i] = (self.x * self.x_l[j][i - 1]) % self.p[j]

    # Computes the hash value of a given substring
    def substring_hash(self, start_index, length, index):
        return (self.hashes[index][start_index + length] - (self.x_l[index][length] * self.hashes[index][start_index]) % self.p[index]) % self.p[index]

    # Returns if both the hash values (both hashes) of both substrings are equal
    def ask(self, a, b, l):
        return (self.substring_hash(a, l, 0) == self.substring_hash(b, l, 0))\
            and (self.substring_hash(a, l, 1) == self.substring_hash(b, l, 1))


s = sys.stdin.readline()
q = int(sys.stdin.readline())
solver = Solver(s)
for i in range(q):
    a, b, l = map(int, sys.stdin.readline().split())
    print("Yes" if solver.ask(a, b, l) else "No")
