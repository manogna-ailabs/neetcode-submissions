class Solution:
    def addBinary(self, a: str, b: str) -> str:
        
        a = a[::-1] 
        b = b[::-1]

        carry = 0
        res = ""

        na, nb = len(a), len(b)
        n = max(na, nb)

        for i in range(n):
            sa = int(a[i]) if i < na else 0
            sb = int(b[i]) if i < nb else 0
            total = sa + sb + carry
            res += str(total % 2)
            carry = total // 2
        if carry:
            res += "1"
        res = "".join(res[::-1])
        return res
