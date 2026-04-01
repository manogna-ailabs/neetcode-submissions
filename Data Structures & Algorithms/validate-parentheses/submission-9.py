class Solution:
    def isValid(self, s: str) -> bool:
        hashmap = {')': '(', '}':'{', ']':'['}

        stack = []
        for ch in s:
            if ch not in hashmap:
                stack.append(ch) #opening
            else:
                if not stack or stack[-1]!=hashmap[ch]:
                    return False
                else: #correct match
                    stack.pop()
        return len(stack)==0
        