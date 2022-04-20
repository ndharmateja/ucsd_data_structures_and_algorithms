# Uses python3
import sys
from collections import namedtuple

Segment = namedtuple('Segment', 'start end')


def optimal_points(segments):
    points = []
    segments = sorted(segments, key=lambda x: x[0])
    optimal_points_helper(segments, points)
    return points


def optimal_points_helper(segments, points):
    if (len(segments)) == 0:
        return
    current_intersection = segments[0]
    for i, s in enumerate(segments):
        if current_intersection[1] < s[0]:
            points.append(current_intersection[1])
            optimal_points_helper(segments[i:], points)
            return
        current_intersection = [max(s[0], current_intersection[0]), min(s[1], current_intersection[1])]
    points.append(current_intersection[1])


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *data = map(int, input.split())
    segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
    points = optimal_points(segments)
    print(len(points))
    print(*points)
