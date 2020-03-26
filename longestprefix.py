"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

"""

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        """
        O(n)
        """
        if strs == []:
            return ""

        a = strs[0]

        for i in range(len(strs)-1):
            b = strs[i+1]
            a = self.findcommon(a, b)

        return a

    def findcommon(self, a, b):
        """
        O(n)
        """
        common = ""
        for i in range(min(len(a), len(b))):
            if a[i] == b[i]:
                common = common + a[i]

            if a[i] != b[i]:
                return common

        return common
