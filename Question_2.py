# Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. 
# The order of the elements may be changed. Then return the number of elements in nums which are 
#not equal to val.
# Consider the number of elements in nums which are not 
# equal to val be k, to get accepted, you need to do the following things:
# Change the array nums such that the first k elements of 
# nums contain the elements which are not # equal to val. 
# The remaining elements of nums are not important as well as the size of nums.
# Return k.

from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        index = 0  # Inicializa o índice para armazenar elementos que não são iguais a val
        for i in range(len(nums)):
            if nums[i] != val:  # Verifica se o elemento atual não é igual a val
                nums[index] = nums[i]  # Coloca o elemento na posição do índice
                index += 1  # Incrementa o índice
        return index  # Retorna o número de elementos que não são iguais a val
