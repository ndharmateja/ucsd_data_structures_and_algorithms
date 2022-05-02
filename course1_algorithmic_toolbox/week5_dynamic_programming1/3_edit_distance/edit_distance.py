# Uses python3
def edit_distance(s, t):
    n = len(s)
    m = len(t)

    d = {}
    d[(0, 0)] = 0
    for i in range(1, n + 1):
        d[(i, 0)] = i
    for i in range(1, m + 1):
        d[(0, i)] = i

    for j in range(1, m + 1):
        for i in range(1, n + 1):
            char1 = s[i - 1]
            char2 = t[j - 1]
            insertion = d[(i, j - 1)] + 1
            deletion = d[(i - 1, j)] + 1
            match = d[(i - 1, j - 1)]
            mismatch = d[(i - 1, j - 1)] + 1

            if char1 == char2:
                d[(i, j)] = min(insertion, deletion, match)
            else:
                d[(i, j)] = min(insertion, deletion, mismatch)

    return d[(n, m)]


if __name__ == "__main__":
    print(edit_distance(input(), input()))
