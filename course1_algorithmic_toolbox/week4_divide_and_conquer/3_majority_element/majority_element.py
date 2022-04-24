# Uses python3
import sys


def get_majority_element(a, left, right):
    a = sorted(a)
    counts = {}
    for x in a:
        counts[x] = counts.get(x, 0) + 1

    max_count = -float('inf')
    max_key = None

    for key, count in counts.items():
        if count > max_count:
            max_count = count
            max_key = key

    return max_key if max_count > len(a) // 2 else -1


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    # a = [2, 3, 9, 2, 2]
    # n = len(a)
    if get_majority_element(a, 0, n - 1) != -1:
        # if get_majority_element(a, 0, n) != -1:
        print(1)
    else:
        print(0)
