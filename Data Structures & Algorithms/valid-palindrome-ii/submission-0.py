class Solution:
    def isPalindrome(self, s:str) -> bool:

        l, r = 0, len(s)-1
        while l<=r:
            if s[l]!=s[r]:
                return False
            l += 1
            r -= 1
        return True

    def validPalindrome(self, s: str) -> bool:

        for i in range(len(s)):
            out = self.isPalindrome(s) or self.isPalindrome(s[:i]+s[i+1:])
            if out:
                return True
        return False
        
