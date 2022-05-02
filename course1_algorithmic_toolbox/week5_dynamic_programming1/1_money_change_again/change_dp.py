# Uses python3


def get_change(m):
    memo = {0: 0}
    for i in range(m):
        for coin in [1, 3, 4]:
            if (i + coin not in memo) or (i + coin in memo and memo[i + coin] > memo[i] + 1):
                memo[i + coin] = memo[i] + 1
    return memo[m]


if __name__ == '__main__':
    m = int(input())
    print(get_change(m))
