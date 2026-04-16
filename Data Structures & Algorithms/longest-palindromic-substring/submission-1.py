class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = 1
        start = 0
        n = len(s)
        for i in range(n):
            # odd length palindromes
            l, r = i, i
            while l<=r and l>=0 and r<n and s[l] == s[r]:
                if r+1-l > res:
                    res = r+1-l
                    start = l
                l, r = l-1, r+1
            # even length palindromes
            l, r = i, i+1
            while l<=r and l>=0 and r<n and s[l] == s[r]:
                if r+1-l > res:
                    res = r+1-l
                    start = l
                l, r = l-1, r+1

        return s[start:start+res]
                 

                    
                

