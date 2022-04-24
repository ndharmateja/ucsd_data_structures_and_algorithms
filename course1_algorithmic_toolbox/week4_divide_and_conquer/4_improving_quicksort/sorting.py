# Uses python3
import sys
import random


def partition3(a, l, r):
    x = a[l]
    k, j = l, l
    for i in range(l + 1, r + 1):
        if a[i] < x:
            if k == j:
                k += 1
                j += 1
                a[i], a[k] = a[k], a[i]
            else:
                k += 1
                j += 1
                a[i], a[k] = a[k], a[i]
                a[i], a[j] = a[j], a[i]
        elif a[i] == x:
            j += 1
            a[i], a[j] = a[j], a[i]
    a[l], a[k] = a[k], a[l]
    return k, j


def partition2(a, l, r):
    x = a[l]
    j = l
    for i in range(l + 1, r + 1):
        if a[i] <= x:
            j += 1
            a[i], a[j] = a[j], a[i]
    a[l], a[j] = a[j], a[l]
    return j


def randomized_quick_sort(a, l, r):
    if l >= r:
        return
    k = random.randint(l, r)
    a[l], a[k] = a[k], a[l]
    # use partition3
    m1, m2 = partition3(a, l, r)
    randomized_quick_sort(a, l, m1 - 1)
    randomized_quick_sort(a, m2 + 1, r)


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    randomized_quick_sort(a, 0, n - 1)
    for x in a:
        print(x, end=' ')
    # for i in range(10):
    #     a = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    #     randomized_quick_sort(a, 0, len(a) - 1)
    #     print(a)

    # a = [9, 7, 8, 10]
    # print(partition3(a, 0, len(a) - 1))
    # print(a)
