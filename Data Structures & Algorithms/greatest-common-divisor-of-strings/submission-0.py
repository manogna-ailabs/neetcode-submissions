class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1 + str2 != str2 + str1:
            return ""

        def gcd(a: int, b: int):
            n = min(a, b)
            for i in range(1, n+1):
                if a % i == 0 and b % i == 0:
                    out = i
            return out
        
        g = gcd(len(str1), len(str2))
        return str1[:g]