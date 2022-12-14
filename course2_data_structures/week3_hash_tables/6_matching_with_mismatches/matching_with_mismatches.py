# python3

import sys
import random


class Solver:

    def __init__(self, k, t, p):
        self.text = t
        self.pattern = p
        self.max_mismatches_allowed = k
        self.text_length = len(self.text)
        self.pattern_length = len(self.pattern)

        # Two hashes for lesser probability of collision
        self.primes = [10**9 + 7, 10**9 + 9]
        self.x = random.randint(0, 10**9)

        # Compute x^l and the hashes of all prefixes for both text and pattern
        self.compute_x_l()
        self.text_prefixes_hashes = self.precompute_prefix_hashes(self.text)
        self.pattern_prefixes_hashes = self.precompute_prefix_hashes(
            self.pattern)

    # Computes x^l % p (for both p1 and p2)
    # for all values of l from 0 to len(text)
    # we can use the same for pattern as well (as len(pattern) <= len(text))
    def compute_x_l(self):
        self.x_l = [[1 for _ in range(self.text_length + 1)]
                    for __ in range(2)]

        i = 1
        while i <= self.text_length:
            for j in range(2):
                self.x_l[j][i] = (self.x * self.x_l[j][i - 1]) % self.primes[j]
            i += 1

    # Computes the hashes (two hashing) of all the prefixes of "string"
    def precompute_prefix_hashes(self, string):
        hashes = [[0 for _ in range(self.text_length + 1)] for __ in range(2)]

        # loop over the characters of the string
        for i, char in enumerate(string, 1):
            # loop for 0th and 1st indexes
            for j in range(2):
                hashes[j][i] = (((self.x * hashes[j][i - 1]) %
                                self.primes[j]) + ord(char)) % self.primes[j]

        return hashes

    # Computes the hash value of a given substring
    # index - 0 or 1 as we are using two hashing (for less probability of collision)
    def substring_hash(self, start_index, end_index, index, hashes):
        length = end_index - start_index + 1
        return (hashes[index][start_index + length] - (self.x_l[index][length] * hashes[index][start_index]) % self.primes[index]) % self.primes[index]

    # Recursive function that computes the number of mismatches
    # for a given 'i' (substring of text at ith position) and the pattern
    #
    # Throws an error if number of mismatches crosses self.max_mismatches_allowed
    # so that we can exit early
    def get_num_mismatches(self, i, low, high):
        # Base case
        if low > high:
            return 0

        # Calculate relative low and high indices for "text"
        text_low_index = low + i
        text_high_index = high + i

        # If the strings are same, we return 0 as number of mismatches
        if self.substring_hash(text_low_index, text_high_index, 0, self.text_prefixes_hashes) == self.substring_hash(low, high, 0, self.pattern_prefixes_hashes) and self.substring_hash(text_low_index, text_high_index, 1, self.text_prefixes_hashes) == self.substring_hash(low, high, 1, self.pattern_prefixes_hashes):
            return 0

        # Calculate mid index and relative mid index for "text"
        mid = (low + high) // 2
        text_mid_index = i + mid

        # If mid char is same, then number of mismatches is 0 otherwise 1
        mismatches = 1 if self.text[text_mid_index] != self.pattern[mid] else 0

        # increment number of mismatches for the left part and
        # if the exceed limit we raise an error
        mismatches += self.get_num_mismatches(i, low=low, high=mid - 1)
        if mismatches > self.max_mismatches_allowed:
            raise Exception("Mismatches exceeded")

        # increment number of mismatches for the right part and
        # if the exceed limit we raise an error
        mismatches += self.get_num_mismatches(i, low=mid + 1, high=high)
        if mismatches > self.max_mismatches_allowed:
            raise Exception("Mismatches exceeded")

        # returns number of mismatches
        return mismatches

    def solve(self):
        positions = []

        # For each possible 'i' we compute number of mismatches
        # and if it is less than limit, we append it to the positions list
        for i in range(self.text_length - self.pattern_length + 1):
            try:
                self.get_num_mismatches(i, low=0, high=self.pattern_length-1)
                positions.append(i)
            except:
                continue

        return positions


# input = [
#     ["0", "ababab", "baaa",],
#     ["1", "ababab", "baaa",],
#     ["1", "xabcabc", "ccc",],
#     ["2", "xabcabc", "ccc",],
#     ["3", "aaa", "xxx",]
# ]


# output = [
#     [], [1], [], [1, 2, 3, 4], [0]
# ]
# for case, expected in zip(input, output):
#     [k, t, p] = case
#     ans = Solver(int(k), t, p).solve()
#     print(ans == expected)

for line in sys.stdin.readlines():
    k, t, p = line.split()
    ans = Solver(int(k), t, p).solve()
    print(len(ans), *ans)
