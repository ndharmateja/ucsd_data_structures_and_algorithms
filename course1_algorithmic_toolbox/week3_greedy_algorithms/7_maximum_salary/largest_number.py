# Uses python3

import sys
from functools import cmp_to_key


def get_bigger(a, b):
    if int(str(a) + str(b)) >= int(str(b) + str(a)):
        return a
    else:
        return b


def compare(a, b):
    if get_bigger(a, b) == a:
        return -1
    else:
        return 1


def largest_number(a):
    # write your code here
    a = sorted(a, key=cmp_to_key(compare))
    res = ""
    for x in a:
        res += str(x)
    return res


# print(largest_number([21, 2]))
if __name__ == '__main__':
    input = sys.stdin.read()
    data = input.split()
    a = data[1:]
    print(largest_number(a))
