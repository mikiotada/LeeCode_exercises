"""
Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.
"""

def isPalindrome(s):
    """
    0(n)
    """
    store = []
    s = s.lower()

    for char in s:
        if char.isalnum():
            store.append(char)

    if len(store) == 0:
            return True

    for i in range((len(store)//2)+1):
        if store[i] != store[-i-1]:
            return False

    return True


def test_isPalindrome():
    assert isPalindrome("race a car") == False
    assert isPalindrome("") == True


test_isPalindrome()
