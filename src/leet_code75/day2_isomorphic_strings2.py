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
        inputs:
            * bbbaaaba
            * aaabbbba

        process:
            index = 0
                s[0] = b
                t[0] = a
                map = {
                    "s": {
                        "b": 1
                    },
                    "t": {
                        "a": 1
                    }
                }

            index = 1
                s[1] = a
                t[1] = b
                map = {
                    "s": {
                        "b": 1
                        "a": 2
                    },
                    "t": {
                        "a": 1
                        "b": 2
                    }
                }

            index = 6
                bbbaaa[b]a
                aaabbb[b]a

                map["s"]["b"] == 1
                map["t"]["b"] == 2
                return False

    """
    mapping = {
        "s": {},
        "t": {},
    }
    last_used_number = 1

    for char_s, char_t in zip(s, t):
        if char_s not in mapping["s"] and char_t not in mapping["t"]:
            mapping["s"][char_s] = last_used_number
            mapping["t"][char_t] = last_used_number
            last_used_number += 1

        try:
            if mapping["s"][char_s] != mapping["t"][char_t]:
                return False
        except KeyError:
            return False

    return True
