# python3

import sys
import random


def precompute_prefix_hashes(string, primes, x):
    n = len(string)
    hashes = [[0 for _ in range(n + 1)] for __ in range(2)]

    # loop over the characters of the string
    for i, char in enumerate(string, 1):
        # loop for 0th and 1st indexes
        for j in range(2):
            hashes[j][i] = (((x * hashes[j][i - 1]) %
                            primes[j]) + ord(char)) % primes[j]

    return hashes


# Computes the hash value of a given substring
def substring_hash(start_index, end_index, index, hashes, x_l, primes):
    length = end_index - start_index + 1
    return (hashes[index][start_index + length] - (x_l[index][length] * hashes[index][start_index]) % primes[index]) % primes[index]


def get_num_mismatches(text, pattern, text_hashes, pattern_hashes, primes, x_l, i, k, low, high):
    if low > high:
        return 0

    text_low_index = low + i
    text_high_index = high + i

    if substring_hash(text_low_index, text_high_index, 0, text_hashes, x_l, primes) == substring_hash(low, high, 0, pattern_hashes, x_l, primes) and substring_hash(text_low_index, text_high_index, 1, text_hashes, x_l, primes) == substring_hash(low, high, 1, pattern_hashes, x_l, primes):
        return 0

    mid = (low + high) // 2
    text_mid_index = i + mid

    mismatches = 1 if text[text_mid_index] != pattern[mid] else 0
    mismatches += get_num_mismatches(text, pattern,
                                     text_hashes, pattern_hashes, primes, x_l, i, k, low=low, high=mid - 1)

    if mismatches > k:
        raise Exception("Mismatches exceeded")

    mismatches += get_num_mismatches(text, pattern,
                                     text_hashes, pattern_hashes, primes, x_l, i, k, low=mid + 1, high=high)
    if mismatches > k:
        raise Exception("Mismatches exceeded")

    return mismatches


def get_partial_match_positions(k, text, pattern, text_hashes, pattern_hashes, x_l, primes):
    positions = []

    n = len(text)
    p = len(pattern)

    for i in range(n - p + 1):
        try:
            get_num_mismatches(text, pattern, text_hashes,
                               pattern_hashes, primes, x_l, i, k, low=0, high=p-1)
            positions.append(i)
        except:
            continue

    return positions


def compute_x_l(text, primes, x):
    n = len(text)
    x_l = [[1 for _ in range(n + 1)] for __ in range(2)]

    i = 1
    while i <= len(text):
        for j in range(2):
            x_l[j][i] = (x * x_l[j][i - 1]) % primes[j]
        i += 1

    return x_l


def solve(k, text, pattern):
    primes = [10**9 + 7, 10**9 + 9]
    x = random.randint(0, 10**9)

    x_l = compute_x_l(text, primes, x)
    text_hashes = precompute_prefix_hashes(text, primes, x)
    pattern_hashes = precompute_prefix_hashes(pattern, primes, x)

    return get_partial_match_positions(k, text, pattern, text_hashes, pattern_hashes, x_l, primes)


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
#     ans = solve(int(k), t, p)
#     print(ans == expected)

for line in sys.stdin.readlines():
    k, t, p = line.split()
    ans = solve(int(k), t, p)
    print(len(ans), *ans)
