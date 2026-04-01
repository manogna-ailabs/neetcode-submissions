class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0,1
        maxL = 1 if len(s)>=1 else 0
        print(len(s))
        while l<=r and r < len(s):
            substring = s[l]
            while r < len(s):
                if s[r] not in substring:
                    substring += s[r]
                    maxL = max(maxL, len(substring))
                else:
                    break
                r += 1       
            l = l+1
            r = l+1
        return maxL
        