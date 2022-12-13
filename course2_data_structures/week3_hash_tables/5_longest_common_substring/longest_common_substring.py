# python3

import sys
from collections import namedtuple
from typing import List
import random

Answer = namedtuple('answer_type', 'i j len')


def poly_hash(string, p, x):
    hash = 0
    n = len(string)
    for i in range(n - 1, -1, -1):
        hash = (hash * x + ord(string[i])) % p
    return hash


# precomputes hashes of all substrings of length 'k' in 'text
def precompute_hashes(text, k, p, x, x_pow_k) -> List[int]:
    n = len(text)
    hashes = [0 for _ in range(n - k + 1)]
    hashes[n-k] = poly_hash(text[n - k:], p, x)
    for i in range(n - k - 1, -1, -1):
        hashes[i] = ((hashes[i + 1] * x) + ord(text[i]) -
                     (ord(text[i + k]) * x_pow_k)) % p
    return hashes


# length of 's' should not be greater than length of 't'
def find_lcs(s, t, primes, x):
    ans = Answer(0, 0, 0)

    low = 1
    high = len(s)
    while low <= high:
        k = (low + high) // 2
        x_pow_k = [1, 1]
        for _ in range(k):
            x_pow_k[0] = (x_pow_k[0] * x) % primes[0]
            x_pow_k[1] = (x_pow_k[1] * x) % primes[1]

        # precompute hashes of s
        s_hashes = [precompute_hashes(s, k, primes[0], x, x_pow_k[0]), precompute_hashes(
            s, k, primes[1], x, x_pow_k[1])]

        # precompute hashes of t
        t_hashes = [precompute_hashes(t, k, primes[0], x, x_pow_k[0]), precompute_hashes(
            t, k, primes[1], x, x_pow_k[1])]

        # Make set of the hashes of 't'
        t_hashes_sets = [set(t_hashes[0]), set(t_hashes[1])]

        # Iterate through the substring hashes of s
        # and see if it exists in the set of t_hashes
        # if it exists, we can update answer
        # and search in [k + 1, high]
        found = False
        for i, (s_hash0, s_hash1) in enumerate(zip(s_hashes[0], s_hashes[1])):
            if s_hash0 in t_hashes_sets[0] and s_hash1 in t_hashes_sets[1]:
                j = t_hashes[0].index(s_hash0)
                found = True
                ans = Answer(i, j, k)
                break

        if found:
            low = k + 1
            continue
        else:
            high = k - 1
            continue

    return ans


def solve(s, t):
    # Switch s and t if 's' is longer than 't'
    # We would only need to build a smaller hash table
    # if we have a smaller 's'
    switch_st: bool = False
    if len(s) > len(t):
        switch_st = True
        s, t = t, s

    # Initialize primes and x
    primes = [10 ** 9 + 7, 10 ** 9 + 9]
    x = random.randint(1, 10 ** 9)

    # solve
    ans = find_lcs(s, t, primes, x)

    # If s and t were switched we switch i and j values
    if switch_st:
        ans = Answer(ans.j, ans.i, ans.len)
    return ans


for line in sys.stdin.readlines():
    s, t = line.split()
    ans = solve(s, t)
    print(ans.i, ans.j, ans.len)
