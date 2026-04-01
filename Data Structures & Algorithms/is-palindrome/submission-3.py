class Solution:
    def isPalindrome(self, s: str) -> bool:
        c = ''

        for ch in s:
            if ord('0') <= ord(ch) <= ord('9'):
                c += ch
            elif ord('a') <= ord(ch) <= ord('z'):
                c += ch
            elif ord('A') <= ord(ch) <= ord('Z'):
                c += ch.lower()
        
        n = len(c)
        if n == 0:
            return True
        
        for i in range(n//2+1):
            if c[i] != c[-(i+1)]:
                return False

        return True

        