import sys
import numpy as np

"""
TASK 01 - 
For the given integer N, print snake matrix.
Odd lines should be increasing, even lines should be decreasing.
"""


def run():
    print("Let's play, give me a number between 1 and 50 and I'll print a snake matrix in that dimensions.\n"
          "Choose a number and press enter:")
    n = int(sys.stdin.readline())
    assert n <= 50
    assert n >= 1

    res_mat = np.array(range(1, n ** 2 + 1))

    double_end = res_mat % (2 * n) == 0
    not_double_end = res_mat % (2 * n) != 0
    single_end = res_mat % n == 0

    change_to_start = np.where(double_end)[0]
    change_to_end = np.where(single_end & not_double_end)[0] + 1
    add_end = np.where(single_end)[0]

    for start_idx, end_idx in zip(change_to_start, change_to_end):
        res_mat[end_idx: start_idx + 1] = np.flip(res_mat[end_idx: start_idx + 1])

    res = list()
    for idx, val in enumerate(res_mat):
        if idx in add_end:
            res.append(str(val) + '\n')
        else:
            res.append(str(val) + ' ')

    print("".join(res))


if __name__ == "__main__":
    run()
