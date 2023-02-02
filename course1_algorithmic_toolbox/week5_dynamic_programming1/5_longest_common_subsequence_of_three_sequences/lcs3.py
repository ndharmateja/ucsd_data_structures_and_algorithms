# Uses python3

import sys


def lcs3(a, b, c, memo={}):
    if len(a) == 0 or len(b) == 0 or len(c) == 0:
        return 0
    key = (len(a), len(b), len(c))
    if key not in memo:
        val1 = lcs3(a[:-1], b, c, memo)
        val2 = lcs3(a, b[:-1], c, memo)
        val3 = lcs3(a, b, c[:-1], memo)
        val4 = lcs3(a[:-1], b[:-1], c, memo)
        val5 = lcs3(a[:-1], b, c[:-1], memo)
        val6 = lcs3(a, b[:-1], c[:-1], memo)
        val7 = lcs3(a[:-1], b[:-1], c[:-1], memo)
        if a[-1] == b[-1] and a[-1] == c[-1]:
            memo[key] = max(val1, val2, val3, val4, val5, val6, val7 + 1)
        else:
            memo[key] = max(val1, val2, val3, val4, val5, val6, val7)
    return memo[key]


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    an = data[0]
    data = data[1:]
    a = data[:an]
    data = data[an:]
    bn = data[0]
    data = data[1:]
    b = data[:bn]
    data = data[bn:]
    cn = data[0]
    data = data[1:]
    c = data[:cn]

    # a = [8, 3, 2, 1, 7]
    # b = [8, 2, 1, 3, 8, 10, 7]
    # c = [6, 8, 3, 1, 4, 7]
    print(lcs3(a, b, c))
