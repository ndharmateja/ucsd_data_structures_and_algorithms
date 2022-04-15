# Uses python3
import sys


def gcd(a, b):
    if b == 0:
        return a
    a1 = a % b
    return gcd(b, a1)


def lcm_naive(a, b):
    return a * b // gcd(a, b)


if __name__ == '__main__':
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(lcm_naive(a, b))
