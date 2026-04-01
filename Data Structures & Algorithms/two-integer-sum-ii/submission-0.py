class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        for i, m in enumerate(numbers[:-1]):
            for j, n in enumerate(numbers[i+1:]):
                if m+n == target:
                    return [i+1, i+j+2]