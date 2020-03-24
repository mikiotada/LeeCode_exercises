"""
The function first discards as many whitespace characters as necessary until the first non-whitespace character is found. Then, starting from this character, takes an optional initial plus or minus sign followed by as many numerical digits as possible, and interprets them as a numerical value.

The string can contain additional characters after those that form the integral number, which are ignored and have no effect on the behavior of this function.

If the first sequence of non-whitespace characters in str is not a valid integral number, or if no such sequence exists because either str is empty or it contains only whitespace characters, no conversion is performed.

If no valid conversion could be performed, a zero value is returned.

"""

# this solution was provided by @caikehe, not my own original solution.

class Solution:
    def myAtoi(self, str):
        str = str.strip()
        if str == "":
            return 0
        if str[0] != "+" and str[0] != "-" and not str[0].isdigit():
            return 0
        else:
            if str[0] in ["+", "-"]:
                sign = str[0]
                res = self.helper(str[1:])
                return min(res, 2147483647) if sign == "+" else max(0-res, -2147483648)
            else: 
                return min(self.helper(str), 2147483647)

    def helper(self, string):
        res = 0
        for s in string:
            if not s.isdigit():
                break
            res = 10 * res + int(s)
        return res
