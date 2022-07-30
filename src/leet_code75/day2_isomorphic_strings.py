"""
205. Isomorphic Strings
Easy

Given two strings s and t, determine if they are isomorphic.
Two strings s and t are isomorphic if the
characters in s can be replaced to get t.

All occurrences of a character must be replaced
with another character while preserving the order of characters.
No two characters may map to the same character,
but a character may map to itself.

Example 1:
    Input: s = "egg", t = "add"
    Output: true

Example 2:
    Input: s = "foo", t = "bar"
    Output: false

Example 3:
    Input: s = "paper", t = "title"
    Output: true

Constraints:
    1 <= s.length <= 5 * 104
    t.length == s.length
    s and t consist of any valid ascii character.
"""


def is_isomorphic(s: str, t: str) -> bool:
    """
    Visualization:
        1. Count character occurrence of s
        2. Count character occurrence of t
        3. Return True if all occurrences match

    Optimization:
        * Can we do it inside one loop?
    """

    # Let's do the simple approach for now
    s_occurrences = _map_occurrences(string=s)
    t_occurrences = _map_occurrences(string=t)
    print(f"s: {s_occurrences}")
    print(f"t: {t_occurrences}")
    return s_occurrences == t_occurrences


def _map_occurrences(string: str) -> list:
    """
    :returns: Examples:
        input: paper
        output: [1, 1, 1, 2]

        input: title
        output: [1, 1, 1, 2]
    """

    occurrences = {}
    for char in string:
        if char not in occurrences:
            occurrences[char] = 0
        occurrences[char] += 1

    print(occurrences)
    """
    At this point, sample value of occurrences:
        input: egg
        output: {'e': 1, 'g': 2}
    I'm sure there's a built in way of this, which is faster.
    But let's try from scratch
    """
    return sorted(occurrences.values())
