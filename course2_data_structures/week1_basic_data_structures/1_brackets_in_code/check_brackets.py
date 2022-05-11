# python3

from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    opening_brackets_stack = []
    for i, char in enumerate(text, 1):
        if char in "([{":
            opening_brackets_stack.append({"index": i, "char": char})
        if char in ")]}":
            if len(opening_brackets_stack) == 0:
                return i
            popped = opening_brackets_stack.pop()["char"]
            if not are_matching(popped, char):
                return i
    if len(opening_brackets_stack) == 0:
        return "Success"
    else:
        return opening_brackets_stack[-1]["index"]


def main():
    text = input()
    mismatch = find_mismatch(text)
    print(mismatch)


if __name__ == "__main__":
    main()
