
# You are given two integer arrays nums1 and nums2, 
# sorted in non-decreasing order, and two integers m and n, representing the 
# number of elements in nums1 and nums2 respectively.
# Merge nums1 and nums2 into a single array sorted in non-decreasing order.
# The final sorted array should not be returned by the function, but instead be stored inside the array nums1. To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements 
# that should be merged, and the last n elements are set to 0 and should be 
# ignored. nums2 has a length of n.


# Importando o tipo 'List' que permite especificar que 'nums1' e 'nums2' são listas de inteiros
from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # Se não houver elementos em nums2 para mesclar, retorne imediatamente
        if n == 0:
            return
        
        # Obtém o comprimento total de nums1 (que deve ser m + n)
        len1 = len(nums1)
        # Define o índice de onde começar a preencher nums1 de trás para frente
        end_idx = len1 - 1
        
        # Mesclar nums1 e nums2 de trás para frente
        while n > 0 and m > 0:
            if nums2[n - 1] >= nums1[m - 1]:
                # Se o elemento atual de nums2 for maior ou igual ao elemento atual de nums1,
                # coloque esse elemento no final de nums1
                nums1[end_idx] = nums2[n - 1]
                n -= 1  # Decrementa o contador de nums2
            else:
                # Caso contrário, coloque o elemento de nums1 no final de nums1
                nums1[end_idx] = nums1[m - 1]
                m -= 1  # Decrementa o contador de nums1
            end_idx -= 1  # Decrementa o índice final
        
        # Se ainda houver elementos em nums2, continue preenchendo nums1 com eles
        while n > 0:
            nums1[end_idx] = nums2[n - 1]
            n -= 1
            end_idx -= 1
