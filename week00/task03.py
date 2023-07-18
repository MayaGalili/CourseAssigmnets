import sys
import numpy as np

"""
TASK 03 - for a given dictionary of words and prefixes, returns up to 10 words 
starting with that prefixes. each prefix match in a separate line
"""


def __check_input(w: str):
    """
    check if words are ASCII only, not empty, and don't contain whitespace
    """
    assert all(ord(c) < 128 for c in w)
    assert ' ' not in w
    assert w != ""


def __read_input_words(f) -> list:
    number_of_words = int(f.readline())
    assert (0 < number_of_words < 5000000)

    print("Please pass here a list of sorted words.\ne.g.:\n"
          "Apple\nAba\nCat\n")
    words = sorted([f.readline().strip() for _ in range(number_of_words)])
    assert len(np.unique(np.array(words))) == len(words)
    for w in words:
        __check_input(w)

    return words


def __print_pref_matches(words, prefix):
    res = list()

    for i in words:

        if i.startswith(prefix):
            if len(res) > 10:
                break
            else:
                res.append(i)
    print(" ".join(res))


def run():
    print("Let's play, You will give me a dictionary of words and a prefix and I will return the relevant "
          "words with that prefix. Cool right?")

    print("Please type here the number of words in your dictionary:")
    f = sys.stdin

    input_words = __read_input_words(f)

    print("Please type here the number of prefix you want to check:")
    number_of_pref = int(f.readline())
    assert (0 < number_of_pref < 1000000)

    print("Please type here the prefixes. one prefix per line:")
    for _ in range(number_of_pref):
        prefix = f.readline().strip()
        assert len(prefix) <= 42
        __check_input(prefix)
        __print_pref_matches(input_words, prefix)


if __name__ == "__main__":
    run()
