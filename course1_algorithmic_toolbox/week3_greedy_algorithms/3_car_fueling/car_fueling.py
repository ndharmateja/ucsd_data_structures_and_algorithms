# python3
import sys


def compute_min_refills(distance, tank, stops):
    # write your code here
    if distance <= tank:
        return 0
    if (len(stops) == 0 and distance > tank) or stops[0] > tank:
        return - 1

    i = 0
    while i < len(stops) - 1:
        if stops[i + 1] > tank:
            break
        i += 1

    current_stop = stops[i]
    remaining_stops = compute_min_refills(distance - stops[i], tank, [stop - current_stop for stop in stops[i + 1:]])
    if remaining_stops == -1:
        return -1
    else:
        return 1 + remaining_stops


if __name__ == '__main__':
    d, m, _, *stops = map(int, sys.stdin.read().split())
    print(compute_min_refills(d, m, stops))
