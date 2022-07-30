from src.leet_code75.day2_subsequence import is_subsequence


class TestSubsequence:
    def test_example1(self):
        assert is_subsequence(s="abc", t="ahbgdc") is True

    def test_example2(self):
        assert is_subsequence(s="axc", t="ahbgdc") is False

    def test_example3(self):
        assert is_subsequence(s="aaaaaa", t="bbaaaa") is False
