# python3

def parent(i):
    return (i - 1) // 2


def left(i):
    return 2 * i + 1


def right(i):
    return 2 * i + 2


def sift_down(i, data, swaps):
    l = left(i)
    r = right(i)

    max_index = i

    if l < len(data) and data[l] < data[max_index]:
        max_index = l
    if r < len(data) and data[r] < data[max_index]:
        max_index = r

    if i != max_index:
        data[i], data[max_index] = data[max_index], data[i]
        swaps.append((i, max_index))
        sift_down(max_index, data, swaps)


def build_heap(data):
    """Build a heap from ``data`` inplace.

    Returns a sequence of swaps performed by the algorithm.
    """
    # The following naive implementation just sorts the given sequence
    # using selection sort algorithm and saves the resulting sequence
    # of swaps. This turns the given array into a heap, but in the worst
    # case gives a quadratic number of swaps.
    #
    swaps = []
    start = parent(len(data) - 1)

    for i in range(start, -1, -1):
        sift_down(i, data, swaps)

    return swaps


def main():
    n = int(input())
    data = list(map(int, input().split()))
    assert len(data) == n

    swaps = build_heap(data)

    print(len(swaps))
    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    main()
