"""
Ordenar do que mais aparece, para o que menos aparece

Exemplo:
aaaaaaaabbccccccccccccc
resultado 
cba
"""
def arrumar(s):
    alph = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    raw_char_count = [0] * len(alph)


    print(raw_char_count)
    for char in s:
        raw_char_count[alph.index(char)] += 1
        
    print(raw_char_count)



arrumar("aan")
    