# python3
from collections import deque

def max_sliding_window_naive(sequence, m):
    maximums = []
    for i in range(len(sequence) - m + 1):
        maximums.append(max(sequence[i:i + m]))

    return maximums


def printMax(arr, n, k):
    Qi = deque()

    maximums = []
    for i in range(k):
        while Qi and arr[i] >= arr[Qi[-1]]:
            Qi.pop()

        Qi.append(i)

    for i in range(k, n):
        maximums.append(int(arr[Qi[0]]))

        while Qi and Qi[0] <= i-k:
            Qi.popleft()

        while Qi and arr[i] >= arr[Qi[-1]]:
            Qi.pop()

        Qi.append(i)

    maximums.append(int(arr[Qi[0]]))
    return maximums


def max_sliding_window_optimal(sequence, m):
    # parsed_sequence = sequence.split()
    return printMax(parsed_sequence, len(parsed_sequence), m)


if __name__ == '__main__':
    n = int(input())
    input_sequence = [int(i) for i in input().split()]
    assert len(input_sequence) == n
    window_size = int(input())

    print(*max_sliding_window_optimal(input_sequence, window_size))

