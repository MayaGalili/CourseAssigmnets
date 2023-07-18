"""
Merge N sorted arrays into 1 sorted array. Read the input and print the result using the provided starter code.


Input
-----

The first line of the input contains one integer N, the number of sorted arrays. The next line contains N integers, the
lengths of the N arrays. The following N lines contain the sorted elements of the arrays, separated by whitespaces.
All elements are integers.


Output
------

A sorted array containing the elements of all N arrays. The result should be output in one line,
with elements separated by whitespaces.


Constraints:
------

1 <= N <= 23’000

For all 1 <= p <= N and all  0 <= k < lenp, where lenp is the length of the array Ap, it holds that:

    0 < len1, …, lenn < 1'000
    the elements Ap[k] are of type int and 0 <= Ap[k] <= 1’000’000
    Ap[i] <= Ap[j] for 0 <= i < j < lenp


Example
-------

Input:

3
2 3 4
1 3
2 4 5
2 3 3 4



Output:

1 2 2 3 3 3 4 4 5



For the example above:

A_1 = [1, 3], A_2 = [2, 4, 5], A_3 = [2, 3, 3, 4];

The result is [1, 2, 2, 3, 3, 3, 4, 4, 5].
"""

import sys


def merge_2_arr(ta, tb) -> list:
    ai = 0
    bi = 0
    a = len(ta)
    b = len(tb)

    assert 0 <= ta[0] and ta[-1] <= 1000000000
    assert 0 <= tb[0] and tb[-1] <= 1000000000

    res = list()
    while ai < a and bi < b:
        if ta[ai] > tb[bi]:
            res.append(tb[bi])
            bi += 1

        elif tb[bi] > ta[ai]:
            res.append(ta[ai])
            ai += 1

        elif tb[bi] == ta[ai]:
            res.append(ta[ai])
            res.append(tb[bi])
            ai += 1
            bi += 1

    while (ai >= a and bi < b) or (ai < a and bi >= b):

        if ai < a and bi >= b:
            res.append(ta[ai])
            ai += 1

        if bi < b and ai >= a:
            res.append(tb[bi])
            bi += 1

    return res


def run(debug_mode: bool):
    if not debug_mode:
        _ = int(sys.stdin.readline())
        lengths = [int(el) for el in sys.stdin.readline().split()]
        arrays = [[int(el) for el in sys.stdin.readline().split()]
                  for _ in lengths]

    else:
        # test 1 -
        # arrays = [[1, 3], [2, 4, 5], [2, 3, 3, 4]]

        # test 6 -
        arrays = [[1, 2, 3]] * 1000

    while len(arrays) > 1:
        arr1 = arrays.pop()
        arr2 = arrays.pop()
        arr3 = merge_2_arr(arr1, arr2)
        arrays.append(arr3)

    merged = arrays.pop()
    res = ' '.join([str(elem) for elem in merged])
    sys.stdout.write(res)

    if debug_mode:
        # test 1 -
        # assert merged == [1, 2, 2, 3, 3, 3, 4, 4, 5]

        # test 6 -
        assert merged == [1] * 1000 + [2] * 1000 + [3] * 1000


if __name__ == "__main__":
    run(False)
