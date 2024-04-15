"""
Given an integer x, return true if x is a palindrome, and false otherwise.
Constraints:
-231 <= x <= 231 - 1
"""
def isPalindrome(self, x):
    if (x < 0) or (x > 2**31 - 1):
        return False
    
    original_x = x
    reverse = 0

    while (x > 0):
        reverse = reverse * 10 + x % 10
        x //= 10

    return (original_x == reverse)

def isPalindrome2(self, x):
    if x < 0:
        return False

    else:
        return str(x) == str(x)[::-1]