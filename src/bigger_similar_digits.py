import itertools


def next_bigger(number: int):
    if number <= 0:
        return -1

    combinations = all_combinations(
        list(str(number)), length=len(str(number)), number=number
    )
    next_bigger_num = None

    for n in combinations:
        if n == number:
            continue
        elif not next_bigger_num:  # and n > number:
            next_bigger_num = n
        elif next_bigger_num > n > number:
            next_bigger_num = n

    if next_bigger_num is None:
        return -1
    return next_bigger_num


def all_combinations(number_list: list, length: int, number: int):
    return [
        int("".join(permutation))
        for permutation in itertools.permutations(number_list, length)
        if int("".join(permutation)) > number
    ]


if __name__ == "__main__":
    print("------------12", next_bigger(12))
    print("------------513", next_bigger(513))
    print("------------2017", next_bigger(2017))
    print("------------9", next_bigger(9))
    print("------------111", next_bigger(111))
    print("------------531", next_bigger(531))
    print("------------123456789", next_bigger(123456789))
