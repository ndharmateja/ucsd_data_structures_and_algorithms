# Uses python3
import sys
from functools import cmp_to_key


NAME = "name"
VALUE = "value"
START = "start"
POINT = "point"
END = "end"


# To sort by values first in increasing order
# if value is same "start" < "point" < "end"
# the above ordering should be followed in the sorted list
def compare(item1, item2):
    if item1[VALUE] != item2[VALUE]:
        return item1[VALUE] - item2[VALUE]
    priority = [END, POINT, START]
    return priority.index(item2[NAME]) - priority.index(item1[NAME])


# We sort all the values (starts, points, ends) in the above ordering
# We iterate over all the items
# We keep counting the number of open segments (#starts - #ends) at any point
# and if we reach a point, we add the number of open segments to its count
# We also store the sorted order of points (by indices)
# so that we can update count accordingly
def fast_count_segments(starts, ends, points):
    cnt = [0] * len(points)

    all = sorted([{NAME: START, VALUE: x} for x in starts] + [{NAME: POINT, VALUE: x}
                 for x in points] + [{NAME: END, VALUE: x} for x in ends], key=cmp_to_key(compare))
    sorted_points_indices = [i[0] for i in sorted(enumerate(points), key=lambda x:x[1])]

    num_left = 0
    point_index = 0
    for item in all:
        if point_index >= len(points):
            break
        if item[NAME] == START:
            num_left += 1
        elif item[NAME] == END:
            num_left -= 1
        else:
            cnt[sorted_points_indices[point_index]] += num_left
            point_index += 1

    return cnt


def naive_count_segments(starts, ends, points):
    cnt = [0] * len(points)
    for i in range(len(points)):
        for j in range(len(starts)):
            if starts[j] <= points[i] <= ends[j]:
                cnt[i] += 1
    return cnt


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    m = data[1]
    starts = data[2:2 * n + 2:2]
    ends = data[3:2 * n + 2:2]
    points = data[2 * n + 2:]
    # use fast_count_segments
    cnt = fast_count_segments(starts, ends, points)
    # cnt = fast_count_segments([0, 7], [5, 10], [1, 6, 11])
    # cnt = fast_count_segments([-10], [10], [-100, 100, 0])
    for x in cnt:
        print(x, end=' ')
