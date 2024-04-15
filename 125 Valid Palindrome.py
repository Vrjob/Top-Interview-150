'''
A phrase is a palindrome if, after converting all uppercase letters into lowercase 
letters and removing all non-alphanumeric characters, it reads the same 
forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

Constraints:

1 <= s.length <= 2 * 10^5
s consists only of printable ASCII characters.
'''
import re

def isPalindrome(self, s):
    """
    :type s: str
    :rtype: bool
    """

    l = len(s)
    left = 0 
    right = l - 1
    while left <= right:
        if not s[left].isalnum():
            left = left + 1
        elif not s[right].isalnum():
            right = right - 1
        else:
            if s[left].lower() == s[right].lower():
                left = left + 1
                right = right - 1
            else:
                return False
    return True

print(isPalindrome(0,"olhee,,,..,hlo"))
