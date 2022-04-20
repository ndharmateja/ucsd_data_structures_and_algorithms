# Uses python3
import sys


def get_optimal_value(capacity, weights, values):
    if capacity == 0:
        return 0
    total_value = 0
    total_weight = 0
    weights, values = zip(*sorted(zip(weights, values), reverse=True,
                                  key=lambda x: x[1] / x[0]))

    return get_optimal_value_helper(capacity, list(weights), list(values))

    # for w, v in zip(weights, values):
    #     if total_weight + w <= capacity:
    #         total_value += v
    #         total_weight += w
    #     else:
    #         fraction = (capacity - total_weight) / w
    #         total_value += fraction * v

    # return total_value


def get_optimal_value_helper(capacity, weights, values):
    if capacity == 0 or len(weights) == 0:
        return 0
    amount = min(weights[0], capacity)
    value = amount * values[0] / weights[0]
    weights.pop(0)
    values.pop(0)

    return value + get_optimal_value_helper(capacity - amount, weights, values)


if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
