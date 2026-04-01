class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        next_great = {}
        stack = []
        for i, n in enumerate(nums2):
            while stack and n>nums2[stack[-1]]:
                prev_index = stack.pop()
                next_great[nums2[prev_index]] = n
            stack.append(i)
        out = []
        for n in nums1:
            if n in next_great:
                out.append(next_great[n])
            else:
                out.append(-1)
        return out