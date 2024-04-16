"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".
"""
def longestCommonPrefix(self, strs):
 # Se a lista estiver vazia, não há prefixo comum, 
 # então retornamos uma string vazia.
    if not strs:
        return ""

    # Iteramos pelos caracteres da primeira string.
    for i, char in enumerate(strs[0]):
        # Verificamos se o caractere é comum a todas as outras strings.
        for s in strs[1:]:
            # Se o índice exceder o comprimento da string atual ou se o caractere não corresponder, 
            # retornamos o prefixo comum encontrado até agora.
            if i >= len(s) or s[i] != char:
                return strs[0][:i]
    
    # Se todas as strings foram verificadas e nenhum caractere diferente foi encontrado, 
    # retornamos a primeira string (ou qualquer outra, pois são todas iguais).
    return strs[0]