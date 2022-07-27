from itertools import combinations

vals = [0, 1, 2, 5, 6, 7, 10, 11, 12]


mapping = {
    "A": 0,
    "B": 1,
    "C": 2,
    "D": 5,
    "E": 6,
    "F": 7,
    "G": 10,
    "H": 11,
    "I": 12,
}
reverse_mapping = {
    0: "A",
    1: "B",
    2: "C",
    5: "D",
    6: "E",
    7: "F",
    10: "G",
    11: "H",
    12: "I",
}
MAX = 10


def build_neighbor_map(current_node: str):
    """
    Pattern:
        right:                      +1
        left:                       -1
        diagonal bottom right:      +6
        diagonal top left:          -6
        diagonal bottom left:       +4
        diagonal top right:         -4
        bottom:                     +5
        top:                        -5
                                    +7
                                    -7
                                    +3
                                    -3

    How to know if neighbor?
        IF
            number is either: all of the above if result is > 0

    """
    int_value = mapping[current_node]
    potential_neighbors = {
        "R": int_value + 1,
        "L": int_value - 1,
        "DBR": int_value + 6,
        "DTL": int_value - 6,
        "DBL": int_value + 4,
        "DTR": int_value - 4,
        "B": int_value + 5,
        "T": int_value - 5,
        # TODO: Update names
        "V": int_value + 7,
        "X": int_value - 7,
        "Y": int_value + 3,
        "Z": int_value - 3,
        "VV": int_value + 9,
        "XX": int_value - 9,
    }

    neighbors = []
    for _direction, value in potential_neighbors.items():
        try:
            vals.index(value)
        except ValueError:
            pass
        else:
            neighbors.append(reverse_mapping[value])

    return neighbors


def count_patterns_from(firstPoint, length, left=set(vals)):

    visited = set([])

    if length == 0 or length >= MAX:
        return 0

    if length == 1:
        return 1

    neighbor_map = {}
    for m in mapping:
        neighbor_map[m] = build_neighbor_map(current_node=m)

    # TODO: Optimize me using recursive approach

    current_point = firstPoint
    current_neighbors = neighbor_map[current_point]
    pattern_count = len(current_neighbors)

    iteration = 2
    print(f"{current_point} - {current_neighbors}")
    while iteration < length:

        for n in current_neighbors:
            if n not in visited:
                print(f"{n} - {neighbor_map[n]}")
                pattern_count += len(neighbor_map[n])
                visited.add(n)

            iteration += 1

    if iteration != length:
        return 0

    return pattern_count
