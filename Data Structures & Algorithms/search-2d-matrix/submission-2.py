class Solution:
    def binary_search(self, nums: List[int], target: int) -> int:
        
        l = 0
        r = len(nums) - 1

        while l <= r:
            mid = l + (r-l)//2
            if target < nums[mid]:
                r = mid - 1
            elif target > nums[mid]:
                l = mid + 1
            else:
                return True
        return False

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        t, b = 0, len(matrix) - 1
        width = len(matrix[0]) - 1

        while t <= b:
            mid = (t + b) // 2
            if target > matrix[mid][width]:
                t = mid + 1
            elif target < matrix[mid][0]:
                b = mid - 1
            else:
                return self.binary_search(matrix[mid], target)
        
        return False