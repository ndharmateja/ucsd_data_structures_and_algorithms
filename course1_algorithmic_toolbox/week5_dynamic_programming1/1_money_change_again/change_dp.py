# Uses python3

def get_change_helper(m, memo={0: 0}):
    if m < 0:
        return float('inf')
    if m not in memo:
        memo[m] = min(get_change_helper(m - 1, memo),
                      get_change_helper(m - 3, memo),
                      get_change_helper(m - 4, memo)) + 1
    return memo[m]


def get_change(m):
    return get_change_helper(m)


if __name__ == '__main__':
    m = int(input())
    print(get_change(m))
