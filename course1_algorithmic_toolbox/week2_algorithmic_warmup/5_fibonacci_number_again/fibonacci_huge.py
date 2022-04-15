# Uses python3
import sys


def get_fibonacci_huge(n, m):
    fib_arr = [0, 1]
    period = [0, 1]

    i = 2
    while True:
        fib_i = fib_arr[i - 1] + fib_arr[i - 2]
        period_remainder_i = fib_i % m

        if period_remainder_i == 1 and period[i - 1] == 0:
            fib_arr.pop()
            period.pop()
            break

        fib_arr.append(fib_i)
        period.append(fib_i % m)
        i += 1

    n1 = n % len(period)
    return period[n1]


if __name__ == '__main__':
    input = sys.stdin.read()
    n, m = map(int, input.split())
    print(get_fibonacci_huge(n, m))
