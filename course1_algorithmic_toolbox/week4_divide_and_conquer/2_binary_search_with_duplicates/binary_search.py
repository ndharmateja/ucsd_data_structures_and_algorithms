def binary_search(array, key):
    return binary_search_helper(array, 0, len(array) - 1, key)


def binary_search_helper(array, left, right, key):
    if left > right:
        return -1
    if left == right:
        if array[left] == key:
            return left
        else:
            return -1
    mid = (left + right) // 2
    if array[mid] == key:
        return binary_search_helper(array, left, mid, key)
    elif array[mid] > key:
        return binary_search_helper(array, left, mid - 1, key)
    else:
        return binary_search_helper(array, mid + 1, right, key)


if __name__ == '__main__':
    num_keys = int(input())
    input_keys = list(map(int, input().split()))
    assert len(input_keys) == num_keys

    num_queries = int(input())
    input_queries = list(map(int, input().split()))
    assert len(input_queries) == num_queries

    # input_keys = [2, 4, 4, 4, 7, 7, 9]
    # input_queries = [9, 4, 5, 2]
    for q in input_queries:
        print(binary_search(input_keys, q), end=' ')
