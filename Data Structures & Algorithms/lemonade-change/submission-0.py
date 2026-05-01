class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        five, ten = 0, 0
        for m in bills:
            if m == 5:
                five += 1
            if m == 10:
                if not five:
                    return False
                ten += 1
                five -= 1
            if m == 20:
                if ten > 0 and five > 0:
                    ten -= 1
                    five -= 1
                elif five >= 3:
                    five -= 3
                else:
                    return False
        return True 