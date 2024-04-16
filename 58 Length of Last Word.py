"""
Given a string s consisting of words and spaces, return the length of the last word in the string.

A word is a maximal 
substring
 consisting of non-space characters only.
"""

def lengthOfLastWord1(self, s):
    new = s.split(" ")

    while("" in new):
        new.remove("")

    return(len(new[-1]))

def lengthOfLastWord2(self, s):
    return len(s.split(None)[-1])