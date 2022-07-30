from src.leet_code75.day2_isomorphic_strings2 import is_isomorphic


class TestIsomorphicStrings:
    def test_example1(self):
        assert is_isomorphic(s="egg", t="add") is True

    def test_example2(self):
        assert is_isomorphic(s="foo", t="bar") is False

    def test_example3(self):
        assert is_isomorphic(s="paper", t="title") is True

    def test_example4(self):
        """
        "bbbaaaba"
        "aaabbbba"
        """
        assert is_isomorphic(s="bbbaaaba", t="aaabbbba") is False

    def test_example5(self):
        """
        "badc"
        "baba"
        """
        assert is_isomorphic(s="badc", t="baba") is False
