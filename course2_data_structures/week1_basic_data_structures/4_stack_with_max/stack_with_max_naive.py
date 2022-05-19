# python3
import sys


class StackWithMax():
    def __init__(self):
        self.__stack = []
        self.max = -float('inf')

    def Push(self, a):
        self.__stack.append(a)
        if a > self.max:
            self.max = a

    def Pop(self):
        if len(self.__stack) == 0:
            return
        popped = self.__stack.pop()
        if popped == self.max:
            self.max = max(self.__stack)

    def Max(self):
        return self.max


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
            assert(0)
