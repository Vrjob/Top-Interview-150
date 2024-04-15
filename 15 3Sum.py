"""
Given an integer array nums, return all the triplets 
[nums[i], nums[j], nums[k]] such that i != j, i != k, 
and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

Constraints:

3 <= nums.length <= 3000
-105 <= nums[i] <= 105
"""

def threeSum(self, nums):
    nums.sort()  # Passo 1: Ordena a lista de números
    resultados = []
    
    for i in range(len(nums) - 2):
        if nums[i] > 0:
            break  # O primeiro número é maior que zero, não há combinações possíveis
        if i > 0 and nums[i] == nums[i - 1]:
            continue  # Passo 3: Ignora números duplicados
        
        left, right = i + 1, len(nums) - 1
        while left < right:
            soma = nums[i] + nums[left] + nums[right]
            if soma == 0:
                resultados.append([nums[i], nums[left], nums[right]])

                # Passo 3: Ignora números duplicados
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1
                left += 1
                right -= 1
                
            elif soma < 0:
                left += 1
            else:
                right -= 1
    
    return resultados

# Exemplo de uso:
nums = [1, 0, 3, 4, 5,-1,0]
resultados = threeSum(0,nums)
print("Somas combinatoriais de 3 números com seus valores:", resultados)

