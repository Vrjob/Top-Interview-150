"""
Given an array of integers citations where citations[i] 
is the number of citations a researcher received for their ith paper, 
return the researcher's h-index.

According to the definition of h-index on Wikipedia: 
The h-index is defined as the maximum value of h such 
that the given researcher has published at least h papers that have each been cited at least h times.

Ou seja, ele quer que retorne o maior numero, desde que na lista, apareca igual ou mais vezes ele e/ou 
valores superiores que o valor dele
"""

def hIndex(self, citations):
        citations.sort(reverse=True)

        h_index = 0
        for i, citation in enumerate(citations):
            if citation >= i + 1:
                h_index = i + 1
            else:
                break

        return h_index

def hIndex2(self, citations):
    """
    :type citations: List[int]
    :rtype: int
    """
    # Ordena as citações em ordem crescente
    citations.sort()
    
    # Inicializa a variável para armazenar o valor máximo do H-Index encontrado
    curr_max = 0
    
    # Inicializa o índice 'i' com o índice do último elemento de 'citations'
    i = len(citations) - 1
    
    # Loop enquanto 'i' for maior ou igual a 0
    while i > -1:
        # Loop para lidar com citações duplicadas
        while i > 0 and citations[i] == citations[i - 1]:
            i -= 1
        
        # Verifica se o número de citações é maior ou igual ao valor atual do H-Index
        if citations[i] >= curr_max:
            # Verifica se o número de citações restantes é maior ou igual ao valor da citação atual
            if len(citations) - i >= citations[i]:
                # Se sim, retorna o valor da citação atual como H-Index
                return citations[i]
            else:
                # Caso contrário, atualiza o valor máximo atual do H-Index
                curr_max = len(citations) - i
        
        # Decrementa 'i' para verificar o próximo elemento de 'citations'
        i -= 1
    
    # Retorna o valor máximo do H-Index encontrado
    return curr_max