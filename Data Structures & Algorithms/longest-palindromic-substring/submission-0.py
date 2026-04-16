class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = 1
        start = 0
        n = len(s)
        # valid_set = set()
        for i in range(n):
            l, r = i, i
            while l<=r and l>=0 and r<n and s[l] == s[r]:
                # valid_set.add((l, r))
                # print(valid_set, start, res)
                if r+1-l > res:
                    res = r+1-l
                    start = l
                l, r = l-1, r+1
            l, r = i, i+1
            while l<=r and l>=0 and r<n and s[l] == s[r]:
                # valid_set.add((l, r))
                # print(valid_set, start, res)
                if r+1-l > res:
                    res = r+1-l
                    start = l
                l, r = l-1, r+1

        return s[start:start+res]
                 

                    
                

