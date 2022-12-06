# python3
import sys


# Takes O(n) auxilary space
# as we are storing another stack with max values
# at every stage
class StackWithMax():
    def __init__(self):
        self.__stack = []
        self.__max = []

    def Push(self, a):
        max_value = a
        if len(self.__stack) != 0 and self.__max[-1] > a:
            max_value = self.__max[-1]

        self.__stack.append(a)
        self.__max.append(max_value)

    def Pop(self):
        if len(self.__stack) == 0:
            return
        self.__stack.pop()
        self.__max.pop()

    def Max(self):
        return self.__max[-1]


if __name__ == '__main__':
    stack = StackWithMax()

    num_queries = int(sys.stdin.readline())
    for _ in range(num_queries):
        query = sys.stdin.readline().split()

        if query[0] == "push":
            stack.Push(int(query[1]))
        elif query[0] == "pop":
            stack.Pop()
        elif query[0] == "max":
            print(stack.Max())
        else:
            assert (0)
