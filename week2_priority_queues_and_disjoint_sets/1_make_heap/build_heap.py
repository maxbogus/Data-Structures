# python3
from math import floor
import heapq


def build_heap(data):
    """Build a heap from ``data`` inplace.

    Returns a sequence of swaps performed by the algorithm.
    """
    # The following naive implementation just sorts the given sequence
    # using selection sort algorithm and saves the resulting sequence
    # of swaps. This turns the given array into a heap, but in the worst
    # case gives a quadratic number of swaps.
    #
    # TODO: replace by a more efficient implementation
    swaps = []
    for i in range(len(data)):
        for j in range(i + 1, len(data)):
            if data[i] > data[j]:
                # print(data[i], data[j])
                swaps.append((i, j))
                data[i], data[j] = data[j], data[i]

    return swaps


def build_heap_fast(data):
    result = []
    size = len(data)

    def get_left(i):
        return (2 * i) + 1

    def get_right(i):
        return (2 * i) + 2

    def heapify_down(i):
        left = get_left(i)
        right = get_right(i)

        smallest = i

        if left < size and data[left] < data[i]:
            smallest = left

        if right < size and data[right] < data[smallest]:
            smallest = right

        if smallest != i:
            result.append((smallest, i))
            data[i], data[smallest] = data[smallest], data[i]
            heapify_down(smallest)

    def buildHeap():
        for i in range(size, -1, -1):
            heapify_down(i)

    buildHeap()

    return result


def main():
    n = int(input())
    data = list(map(int, input().split()))
    assert len(data) == n

    # swaps = build_heap(data)
    swaps = build_heap_fast(data)

    print(len(swaps))
    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    main()
