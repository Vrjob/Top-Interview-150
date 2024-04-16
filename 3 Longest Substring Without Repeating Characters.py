"""
Given a string s, find the length of the longest 
substring without repeating characters.
"""

def lengthOfLongestSubstring(self, s):
    # Inicializa uma lista vazia para armazenar os caracteres da substring atual.
    lista = []
    # Inicializa uma variável para armazenar o comprimento máximo encontrado.
    max_length = 0

    # Percorre cada caractere na string 's'.
    for i in s:
        # Verifica se o caractere atual já está na lista.
        if i in lista:
            # Se o caractere estiver na lista, encontra o índice desse caractere na lista.
            index = lista.index(i)
            # Redefine a lista para começar depois do índice do caractere repetido.
            lista = lista[index + 1:]

        # Adiciona o caractere atual à lista.
        lista.append(i)
        # Atualiza o comprimento máximo encontrado, comparando com o comprimento atual da lista.
        max_length = max(max_length, len(lista))

    # Retorna o comprimento máximo encontrado.
    return max_length

print(lengthOfLongestSubstring(0,"dvdf"))
