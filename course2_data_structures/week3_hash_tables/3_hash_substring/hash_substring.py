# python3
import random


def read_input():
    return (input().rstrip(), input().rstrip())


def print_occurrences(output):
    print(' '.join(map(str, output)))


def pow(x, k, p):
    out = 1
    for _ in range(k):
        out = (out * x) % p
    return out


def poly_hash(string, p, x):
    hash = 0
    n = len(string)
    for i in range(n - 1, -1, -1):
        hash = (hash * x + ord(string[i])) % p
    return hash


# Precomputes hashes of all the substrings of length k
# using the recurrence relation
# hashes[i] = (x * hashes[i + 1] + T[i] - (T[i + k] * x^k)) % p
def precompute_hashes(text, k, p, x, x_pow_k):
    n = len(text)
    hashes = [0 for _ in range(n - k + 1)]
    hashes[n-k] = poly_hash(text[n - k:], p, x)
    for i in range(n - k - 1, -1, -1):
        hashes[i] = ((hashes[i + 1] * x) + ord(text[i]) -
                     (ord(text[i + k]) * x_pow_k)) % p
    return hashes


def get_occurrences(pattern, text):
    # Rabin Karp algorithm

    # Initialize p and x
    p = 10 ** 9 + 7
    x = random.randint(1, p - 1)
    x = 7
    n = len(text)  # text length
    k = len(pattern)  # substring length

    # Compute x^k
    x_pow_k = pow(x, k, p)

    # compute hash of pattern and precompute hashes
    p_hash = poly_hash(pattern, p, x)
    hashes = precompute_hashes(text, k, p, x, x_pow_k)

    positions = []
    for i in range(0, n-k+1):
        if hashes[i] != p_hash:
            continue
        if text[i: i+k] == pattern:
            positions.append(i)
    return positions


if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))
