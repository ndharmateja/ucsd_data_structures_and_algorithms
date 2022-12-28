# Uses python3

import sys


def lcs2(a, b, memo={}):
    if len(a) == 0 or len(b) == 0:
        return 0
    key = (len(a), len(b))
    if key not in memo:
        val1 = lcs2(a[:-1], b, memo)
        val2 = lcs2(a, b[:-1], memo)
        val3 = lcs2(a[:-1], b[:-1], memo)
        if a[-1] == b[-1]:
            memo[key] = max(val1, val2, val3 + 1)
        else:
            memo[key] = max(val1, val2, val3)
    return memo[key]


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))

    n = data[0]
    data = data[1:]
    a = data[:n]

    data = data[n:]
    m = data[0]
    data = data[1:]
    b = data[:m]

    print(lcs2(a, b))
