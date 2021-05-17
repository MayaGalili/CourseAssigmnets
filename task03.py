import sys
import numpy as np


def __check_input(w: str):
    """
    check if words are ASCII only, not empty, and don't contain whitespace
    """
    assert all(ord(c) < 128 for c in w)
    assert not ' ' in w
    assert w != ""


def __read_input_words(f) -> list:
    number_of_words = int(f.readline())
    assert (0 < number_of_words < 5000000)

    words = sorted([f.readline().strip() for _ in range(number_of_words)])
    assert len(np.unique(np.array(words))) == len(words)
    for w in words:
        __check_input(w)

    return words


def __print_pref_matches(words, prefix):
    res = list()
    for i in words:
        if prefix in i:
            if len(res) > 10:
                break
            else:
                res.append(i)
    print(" ".join(res))


def run():
    f = sys.stdin
    input_words = __read_input_words(f)
    number_of_pref = int(f.readline())
    assert (0 < number_of_pref < 1000000)
    for _ in range(number_of_pref):
        prefix = f.readline().strip()
        assert len(prefix) <= 42
        __check_input(prefix)
        __print_pref_matches(input_words, prefix)


if __name__ == "__main__":
    run()
