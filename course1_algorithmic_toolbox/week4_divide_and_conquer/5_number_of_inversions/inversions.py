import sys


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

    for k in range(i, mid + 1):
        b[k] = a[k]
    for k in range(j, right + 1):
        b[k] = a[k]

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


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    b = n * [0]

    print(get_number_of_inversions(a, b, 0, len(a) - 1))

    # n = 5
    # a = [2, 3, 9, 2, 9]
    # b = n * [0]
    # print(merge_and_get_number_of_split_inversions(a, b, 0, len(a) - 1))
    # print(get_number_of_inversions(a, b, 0, len(a) - 1))
    # print(a)
    # print(b)
