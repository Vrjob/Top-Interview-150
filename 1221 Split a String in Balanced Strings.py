"""
Balanced strings are those that have an equal quantity of 'L' and 'R' characters.

Given a balanced string s, split it into some number of substrings such that:

Each substring is balanced.
Return the maximum number of balanced strings you can obtain.
"""

def balancedStringSplit(self, s):
    if len(s) == 0:
        return 0
    r = 0
    l = 0
    
    stg = 0

    for i in range(len(s)):
        if (s[i] == 'R'):
            r += 1

        elif (s[i] == 'L'):
            l += 1

        if (r == l):
            stg += 1
            
    return stg

balancedStringSplit(0,"RLRRRLLRLL")



        
