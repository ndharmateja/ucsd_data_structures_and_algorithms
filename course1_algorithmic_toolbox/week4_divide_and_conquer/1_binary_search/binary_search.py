def binary_search(keys, query):
    # write your code here
    return binary_search_helper(keys, 0, len(keys) - 1, query)


def binary_search_helper(keys, low, high, query):
    if high < low:
        return -1
    mid = low + (high - low) // 2
    if keys[mid] == query:
        return mid
    elif keys[mid] > query:
        return binary_search_helper(keys, low, mid - 1, query)
    else:
        return binary_search_helper(keys, mid + 1, high, query)


if __name__ == '__main__':
    num_keys = int(input())
    input_keys = list(map(int, input().split()))
    assert len(input_keys) == num_keys

    num_queries = int(input())
    input_queries = list(map(int, input().split()))
    assert len(input_queries) == num_queries

    for q in input_queries:
        print(binary_search(input_keys, q), end=' ')

    # print(binary_search([1, 5, 8, 12, 13], 8))
    # print(binary_search([1, 5, 8, 12, 13], 1))
    # print(binary_search([1, 5, 8, 12, 13], 23))
    # print(binary_search([1, 5, 8, 12, 13], 1))
    # print(binary_search([1, 5, 8, 12, 13], 11))
