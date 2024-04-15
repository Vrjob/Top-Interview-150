"""
Desenvolva uma função, usando sua linguagem de preferência, 
que receba uma string como argumento. 
Essa função deve percorrer a string 
removendo a primeira instância de cada letra do alfabeto indo de A-Z, 
repita esse processo até a string ficar vazia e então retorne a string 
logo antes da ultima instancia do processo rodar. 
Exemplo:

str = "aabbcccad"
As letras em maiúsculo serão as removidas:

1 - AaBbCccaD
resultado: "abcca"

2 - ABCca
resultado: "ca"

3 - CA
resultado: ""

A função deve retornar "ca", pois é o ultimo estado da string antes de se tornar vazia
"""

def davi(str):
    alph = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    raw_char_count = [0] * 26
    str_char_count = []
    response = []
    
    for char in str:
        raw_char_count[alph.index(char)] += 1
        str_char_count.append(raw_char_count[alph.index(char)])
    
    max_app = max(str_char_count)
    
    for i in range(len(str_char_count)):
        if str_char_count[i] == max_app:
            response.append(str[i])
    
    return ''.join(response)

print(davi("aabbccciiiod"))