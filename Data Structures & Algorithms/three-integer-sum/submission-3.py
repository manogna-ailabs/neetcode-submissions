class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, 1
        pairs = []
        while l < len(numbers)-1:
            r = l+1
            while r < len(numbers):
                if numbers[l] + numbers[r] == target:
                    pairs.append([numbers[l], numbers[r]])
                r += 1
            l += 1
        return pairs

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        out = []
        for i in range(len(nums)):
            target = -nums[i]
            twosum = self.twoSum(nums[i+1:], target)
            if twosum:
                for pair in twosum:
                    triplet = [nums[i], pair[0], pair[1]]
                    if triplet not in out:
                        out.append(triplet)
        return out






