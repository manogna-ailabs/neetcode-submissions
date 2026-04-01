class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0,1
        maxL = 1 if len(s)>0 else 0
        while l<=r and r<len(s):
            substring = s[l]
            while s[r] not in substring and r<len(s):
                substring += s[r]
                r+=1
                maxL = max(maxL, len(substring))
                if r == len(s):
                    break
            l = l+1
            r = l+1
        return maxL