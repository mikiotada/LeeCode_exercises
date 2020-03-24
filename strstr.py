"""
Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.
"""


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        """"
        O(n)
        ""
        if needle.strip() == '':
            return 0

        for i in range(len(haystack)):
            len_needle = len(needle)
            if haystack[i:i+len_needle] == needle:
                return i

        return -1
