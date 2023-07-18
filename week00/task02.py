import sys

"""
TASK 02 - 
Merge two sorted arrays into one sorted array.

"""


def run():
    print("Let's play, give me two sorted arrays and I'll merge them into one sorted array in no time.")

    print("Please type the size of your tow input list, separated by space (e.g. '2 3') and press Enter:")
    a, b = map(int, sys.stdin.readline().split())
    assert 0 <= a <= 10000000
    assert 0 <= b <= 10000000

    print("Please type the first list, press enter after each of the its elements"
          " (e.g. '2' -> enter -> '3') and press Enter:")
    ta = [int(sys.stdin.readline()) for _ in range(a)]

    print("Please type the second list, press enter after each of the its elements"
          " (e.g. '1' -> enter -> '4' -> enter -> '5') and press Enter:")
    tb = [int(sys.stdin.readline()) for _ in range(b)]

    ai = 0
    bi = 0

    assert 0 <= ta[0] and ta[-1] <= 1000000000
    assert 0 <= tb[0] and tb[-1] <= 1000000000

    print("Here is the sorted merged list:")
    while ai < a and bi < b:
        if ta[ai] > tb[bi]:
            print(tb[bi])
            bi += 1

        elif tb[bi] > ta[ai]:
            print(ta[ai])
            ai += 1

        elif tb[bi] == ta[ai]:
            print(ta[ai])
            ai += 1
            bi += 1

    while (ai >= a and bi < b) or (ai < a and bi >= b):

        if ai < a and bi >= b:
            print(ta[ai])
            ai += 1

        if bi < b and ai >= a:
            print(tb[bi])
            bi += 1


if __name__ == "__main__":
    run()
