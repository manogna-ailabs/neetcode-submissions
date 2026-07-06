class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        l, r = 0, n - 1

        # Find pivot
        while l < r:
            mid = l + (r - l) // 2
            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid

        pivot = l

        # Restore search boundaries
        if nums[pivot] <= target <= nums[n - 1]:
            l, r = pivot, n - 1
        else:
            l, r = 0, pivot - 1

        # Standard binary search
        while l <= r:
            mid = l + (r - l) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1

        return -1 
















        l, r  = 0, len(nums) - 1 

        while l<=r:
            m = (l+r)//2
            print(nums[l], nums[m], nums[r])
            if target == nums[m]:
                return m
            # If left half is sorted
            if nums[l] <= nums[m]:
                if nums[l] <= target < nums[m]:
                    r = m - 1
                else:
                    l = m + 1
            else:
                if nums[m] < target <= nums[r]:
                    l = m + 1
                else:
                    r = m - 1

        return -1