"""
Given an input string s, reverse the order of the words.

A word is defined as a sequence of non-space characters. 
The words in s will be separated by at least one space.

Return a string of the words in reverse order concatenated by a single space.

Note that s may contain leading or trailing spaces or multiple spaces between two words. 
The returned string should only have a single space separating the words. Do not include any extra spaces.
"""
import re
def reverseWords(self, s):
    s = re.sub(' +', ' ', s)

    reversed = []
    words = s.split(' ')

    for word in words:

        if word == ' ':
            if reversed:
                reversed.pop()
        else:
            reversed.append(word)
            

    reversed.reverse()
    new = ' '.join(reversed)
    if new[0] == " ":
        return(new[1:])
    else:
        return(new)      
    
def reverseWords2(self, s):
    return " ".join(s.split()[::-1])  
print(reverseWords(0,"  o amanha vem  1 "))
