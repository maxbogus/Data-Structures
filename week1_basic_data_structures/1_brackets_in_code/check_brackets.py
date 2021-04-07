# python3

from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    opening_brackets_stack = []
    for i, next in enumerate(text):
        if next in "([{":
            # Process opening bracket, write your code here
            opening_brackets_stack.append([next, i])
        if next in ")]}":
            # Process closing bracket, write your code here
            if len(opening_brackets_stack) == 0:
                return i + 1
            last_element, last_element_index = opening_brackets_stack.pop()
            if (last_element == '[' and next != ']') or (last_element == '(' and next != ')') or (last_element == '{' and next != '}'):
                return i + 1
    return 'Success' if len(opening_brackets_stack) == 0 else opening_brackets_stack[0][1]+1


def main():
    text = input()
    # mismatch = find_mismatch(text)
    # Printing answer, write your code here
    # print(text, mismatch)
    print(find_mismatch(text))


if __name__ == "__main__":
    main()
