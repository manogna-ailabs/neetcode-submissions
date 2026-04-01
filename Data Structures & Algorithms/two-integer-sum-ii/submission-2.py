class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, 1
        while l < len(numbers)-1:
            r = l+1
            while r < len(numbers):
                if numbers[l] + numbers[r] == target:
                    return [l+1, r+1]
                r += 1
            l += 1        


