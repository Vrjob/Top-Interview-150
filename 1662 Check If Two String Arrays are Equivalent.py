"""
Given two string arrays word1 and word2, 
return true if the two arrays represent the same string, and false otherwise.

A string is represented by an array if the array elements concatenated in order forms the string.
"""
def arrayStringsAreEqual(self, word1, word2):
    return "".join(word1) == "".join(word2)

self = 0
word1 = ["ab", "c"]
word2 = ["a", "bc"]

print(arrayStringsAreEqual(self, word1, word2))