# Uses python3


def optimal_summands(n):
    summands = []
    # write your code here
    if n <= 2:
        return [n]
    for i in range(1, n):
        sum_i = i * (i + 1) // 2
        if sum_i > n:
            summands[-1] += n - sum(summands)
            break
        else:
            summands.append(i)

    return summands


if __name__ == '__main__':
    n = int(input())
    summands = optimal_summands(n)
    print(len(summands))
    for x in summands:
        print(x, end=' ')
