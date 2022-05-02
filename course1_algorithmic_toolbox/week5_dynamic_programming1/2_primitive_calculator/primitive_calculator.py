# Uses python3


def optimal_sequence(n):
    path = {1: {1}}
    optimal_sequence_helper(n, path)
    return path[n]


def optimal_sequence_helper(n, path):
    for i in range(1, n):
        if (i + 1 not in path) or (i + 1 in path and len(path[i + 1]) > len(path[i]) + 1):
            path[i + 1] = [*path[i], i + 1]
        if (i * 2 not in path) or (i * 2 in path and len(path[i * 2]) > len(path[i]) + 1):
            path[i * 2] = [*path[i], i * 2]
        if (i * 3 not in path) or (i * 3 in path and len(path[i * 3]) > len(path[i]) + 1):
            path[i * 3] = [*path[i], i * 3]


n = int(input())
sequence = list(optimal_sequence(n))
print(len(sequence) - 1)
for x in sequence:
    print(x, end=' ')
