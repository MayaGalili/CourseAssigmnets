import sys

"""
TASK 02 - 
Merge two sorted arrays into one sorted array.

"""


def run():
    a, b = map(int, sys.stdin.readline().split())
    assert 0 <= a <= 10000000
    assert 0 <= b <= 10000000

    ta = [int(sys.stdin.readline()) for _ in range(a)]
    tb = [int(sys.stdin.readline()) for _ in range(b)]

    ai = 0
    bi = 0

    assert 0 <= ta[0] and ta[-1] <= 1000000000
    assert 0 <= tb[0] and tb[-1] <= 1000000000

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
