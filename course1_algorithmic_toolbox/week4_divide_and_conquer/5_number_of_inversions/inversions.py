import sys
import random


def merge_and_get_number_of_split_inversions(a, b, left, right):
    if left == right:
        return 0
    mid = (left + right) // 2
    inversions = 0
    i = left
    j = mid + 1

    # Use 'b' as extra array for inserting smaller of compared elements
    while i <= mid and j <= right:
        if a[i] <= a[j]:
            b[left + (i - left + j - (mid + 1))] = a[i]
            i += 1
        else:
            inversions += mid - i + 1
            b[left + (i - left + j - (mid + 1))] = a[j]
            j += 1

    if i <= mid:
        for k in range(i, mid + 1):
            b[left + (k - left + j - (mid + 1))] = a[k]
    if j <= right:
        for k in range(j, right + 1):
            b[left + (i - left + k - (mid + 1))] = a[k]

    for k in range(left, right + 1):
        a[k] = b[k]

    return inversions


def get_number_of_inversions(a, b, left, right):
    number_of_inversions = 0
    if right == left:
        return number_of_inversions
    mid = (left + right) // 2
    left_inversions = get_number_of_inversions(a, b, left, mid)
    right_inversions = get_number_of_inversions(a, b, mid + 1, right)
    split_inversions = merge_and_get_number_of_split_inversions(a, b, left, right)
    return left_inversions + right_inversions + split_inversions


def get_number_of_inversions_brute(a):
    inversions = 0
    for i in range(len(a)):
        for j in range(i):
            if a[j] > a[i]:
                inversions += 1
    return inversions


def stress_test():
    for _ in range(10000):
        x = random.randint(1, 1000)
        a = random.sample(list(range(1, x + 1)), random.randint(1, x))
        inv_b = get_number_of_inversions_brute(a)
        inv_a = get_number_of_inversions(a[:], [0 for _ in a], 0, len(a) - 1)
        if inv_a != inv_b:
            print("Failed Test Case:")
            print(f"Array: {a}")
            print(f"Actual: {inv_b} Got: {inv_a}")
            return
    print("All tests passed")


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    b = n * [0]

    print(get_number_of_inversions(a, b, 0, len(a) - 1))

    # stress_test()
    # a = [18, 3]
    # n = len(a)
    # b = n * [0]
    # print(get_number_of_inversions(a, b, 0, len(a) - 1))
    # print(merge_and_get_number_of_split_inversions(a, b, 0, len(a) - 1))
    # print(a)
    # print(b)
