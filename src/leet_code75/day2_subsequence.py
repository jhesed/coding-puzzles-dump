"""
392. Is Subsequence
(Easy)

Given two strings s and t,
return true if s is a subsequence of t, or false otherwise.

A subsequence of a string is a new string that
is formed from the original string by deleting
some (can be none) of the characters without
disturbing the relative positions of the
remaining characters. (i.e., "ace"
is a subsequence of "abcde" while "aec" is not).


Example 1:
    Input: s = "abc", t = "ahbgdc"
    Output: true

Example 2:
    Input: s = "axc", t = "ahbgdc"
    Output: false

Constraints:
    0 <= s.length <= 100
    0 <= t.length <= 104
    s and t consist only of lowercase English letters.


Follow up: Suppose there are lots of incoming s,
say s1, s2, ..., sk where k >= 109,
and you want to check one by one to see
if t has its subsequence.
In this scenario, how would you change your code?
"""


def is_subsequence(s: str, t: str) -> bool:
    """
    Visualization:
        inputs:
            * s = abc
            * t = ahbgdc

        Terminating condition:
            * Loop until there's remaining character in t

        Process:
            s_index = 0
            t_index = 0
            s[0] = a
            t[0] = a
            match:
                increment s_index
                increment t_index

            s_index = 1
            t_index = 1
            s[1] = b
            t[1] = h
            doesn't match:
                increment t_index. Compare again
    """

    t_index = 0

    for s_char in s:

        try:
            while s_char != t[t_index]:
                t_index += 1
        except IndexError:
            return False
        else:
            t_index += 1

    return True
