# python3
import re

def read_input():
    return input().rstrip(), input().rstrip()


def print_occurrences(output):
    print(' '.join(map(str, output)))


def get_occurrences(pattern, text):
    return [
        i
        for i in range(len(text) - len(pattern) + 1)
        if text[i:i + len(pattern)] == pattern
    ]

def get_occurrences_naive(pattern, text):
    return [m.start(0) for m in re.finditer(pattern, text)]


if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))

