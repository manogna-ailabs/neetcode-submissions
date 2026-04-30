class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        out = []
        carry = 1
        for n in digits[::-1]:
            sum_n = n + carry
            out += [sum_n % 10]
            carry = sum_n // 10
        if carry:
            out += [carry]
        return out[::-1] 
