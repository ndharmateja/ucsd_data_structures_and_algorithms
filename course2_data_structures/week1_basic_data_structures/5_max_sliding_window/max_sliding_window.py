# python3
from collections import deque
from typing import List


def max_sliding_window(sequence: List[int], m: int) -> List[int]:
    outputs = []

    # we store the indices
    queue = deque()

    # start and end indices of the sliding window (inclusive)
    start = end = 0

    while end < len(sequence):
        # Remove all elements on right that are smaller than the current value
        while len(queue) > 0 and sequence[queue[-1]] < sequence[end]:
            queue.pop()

        # Add new value to queue
        queue.append(end)

        # Remove left most value if out of bounds
        if (queue[0] < start):
            queue.popleft()

        if end + 1 >= m:
            start += 1
            outputs.append(sequence[queue[0]])

        end += 1

    return outputs


if __name__ == '__main__':
    n = int(input())
    input_sequence = [int(i) for i in input().split()]
    assert len(input_sequence) == n
    window_size = int(input())

    print(*max_sliding_window(input_sequence, window_size))
