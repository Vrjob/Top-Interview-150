"""
Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

A subsequence of a string is a new string that is formed from the original 
string by deleting some (can be none) of the characters without disturbing 
the relative positions of the remaining characters. 
(i.e., "ace" is a subsequence of "abcde" while "aec" is not).
"""
def isSubsequence(s, t):
    # Inicializa os ponteiros para ambas as strings
    i, j = 0, 0
    
    # Itera por ambas as strings
    while i < len(s) and j < len(t):
        # Se os caracteres correspondentes, avança o ponteiro na string de origem
        if s[i] == t[j]:
            i += 1
        # Sempre avança o ponteiro na string alvo
        j += 1
        
    # Se iteramos por toda a string de origem, é uma subsequência
    return i == len(s)