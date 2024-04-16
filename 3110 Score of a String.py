"""
You are given a string s. 
The score of a string is defined as the sum of the absolute difference 
between the ASCII values of adjacent characters.

Return the score of s.
"""
def scoreOfString(self, s):
    abs_diff = 0
    for i in range(len(s) - 1):
        diff = abs(ord(s[i]) - ord(s[i+1]))
        abs_diff += diff
    return abs_diff