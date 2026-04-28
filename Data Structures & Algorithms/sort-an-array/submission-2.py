class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        """ Insertion Sort
        - Insert each element in its position. Push elements to the right.
        """
        n = len(nums)
        for i in range(1, n):
            key = nums[i]
            j = i - 1
            while j >= 0 and nums[j] > key:
                nums[j+1] = nums[j]
                j -= 1
            nums[j+1] = key
        return nums

        """ Selection Sort
        - Pick smallest element and place it in the front
        """
        n = len(nums)
        for i in range(n):
            min_idx = i
            for j in range(i+1, n):
                if nums[j] < nums[min_idx]:
                    min_idx = j
            nums[i], nums[min_idx] = nums[min_idx], nums[i]
        return nums



        """ Bubble sort:
        - Largest element bubbles to the last in each pass.
        - n-i-1 avoids sorting already sorted elements in the end.
        """
        n = len(nums)
        for i in range(n):
            for j in range(n - i - 1):
                if nums[j]>nums[j+1]:
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]
        return nums
