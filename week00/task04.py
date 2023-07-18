import sys

"""
TASK 04 - 
for a given airports with direct flights between them and trips, returns all flights from an origin to a 
destination airports with exactly one stopover between them sorted lexicographically.
One line for each trip.
"""


def __check_input_airport(w: str):
    """
    check if words are ASCII only, not empty, and don't contain whitespace
    """
    assert all(ord(c) < 128 for c in w)
    assert ' ' not in w
    assert w is not None
    assert type(w) is str
    assert len(w) <= 4
    assert " " not in w


def __validate_input_number(input_sz: int):
    assert input_sz is not None
    assert (type(input_sz) == int)
    assert (0 < input_sz < 1000000)


def __read_input(f) -> [dict, dict]:
    number_of_flights = int(f.readline())
    __validate_input_number(number_of_flights)

    orig_dict = dict()
    dest_dict = dict()

    for _ in range(number_of_flights):
        fr, to = f.readline().split()
        __check_input_airport(fr)
        __check_input_airport(to)

        if fr in orig_dict:
            orig_dict[fr] = orig_dict[fr] + [to]
        else:
            orig_dict[fr] = [to]

        if to in dest_dict:
            dest_dict[to] = dest_dict[to] + [fr]
        else:
            dest_dict[to] = [fr]

    return orig_dict, dest_dict


def __print_stopovers(f, orig_dict, dest_dict):
    fr, to = f.readline().split()
    if fr in orig_dict and to in dest_dict:
        inter = sorted(set(orig_dict[fr]).intersection(set(dest_dict[to])))
        print(" ".join(inter))
    else:
        print("")


def run():
    f = sys.stdin
    orig_dict, dest_dict = __read_input(f)

    number_of_trips = int(f.readline())
    __validate_input_number(number_of_trips)

    for _ in range(number_of_trips):
        __print_stopovers(f, orig_dict, dest_dict)


if __name__ == "__main__":
    run()
