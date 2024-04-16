"""
Given n non-negative integers representing an elevation map where 
the width of each bar is 1, compute how much water it can trap after raining.

Esse problema é clássico e pode ser resolvido usando a técnica de "Two Pointers" (dois ponteiros).

A ideia principal é percorrer a lista de alturas duas vezes: 
uma vez da esquerda para a direita e outra vez da direita para a esquerda. 
Em cada iteração, mantemos o máximo da altura encontrada até agora em cada direção. 
Em seguida, calculamos a quantidade de água que pode ser armazenada em cada posição, 
que é determinada pela diferença entre a altura mínima das paredes à esquerda e à direita, 
e a altura atual da parede.

Somamos essas quantidades de água para cada posição e obtemos o total de água armazenada.

Aqui está a implementação em Python:
"""
def trap(self,height):
    # Verifica se a lista de alturas está vazia
    if not height:
        return 0
    
    n = len(height)
    
    # Inicializa duas listas para armazenar as alturas máximas à esquerda e à direita de cada posição
    left_max = [0] * n
    right_max = [0] * n
    water = 0
    
    # Preenche a lista left_max
    left_max[0] = height[0]
    for i in range(1, n):
        # Para cada posição, armazena a altura máxima encontrada até aquela posição à esquerda
        left_max[i] = max(left_max[i - 1], height[i])
    
    # Preenche a lista right_max
    right_max[n - 1] = height[n - 1]
    for i in range(n - 2, -1, -1):
        # Para cada posição, armazena a altura máxima encontrada até aquela posição à direita
        right_max[i] = max(right_max[i + 1], height[i])
    
    # Calcula a quantidade de água armazenada em cada posição
    for i in range(n):
        # A quantidade de água armazenada em cada posição é a diferença entre a altura mínima das paredes à esquerda e à direita e a altura atual da parede
        water += min(left_max[i], right_max[i]) - height[i]
    
    return water