"""
You are given a 0-indexed array of strings words and a character x.

Return an array of indices representing the words that contain the character x.

Note that the returned array may be in any order.

Example:
    Input: words = ["abc","bcd","aaaa","cbc"], x = "a"
    Output: [0,2]
    Explanation: "a" occurs in "abc", and "aaaa". Hence, we return indices 0 and 2.
"""
def findWordsContaining(self, words, x):
    listFinal = []
    conta = 0
    for i in words:
        if x in i:
            listFinal.append(conta)
        conta += 1

    return listFinal