class Solution:
    def isValid(self, s: str) -> bool:
        hashmap = {')': '(', '}':'{', ']':'['}
        if len(s)==1:
            return False

        stack = []
        for ch in s:
            if ch in hashmap and len(stack)>0:
                if hashmap[ch] == stack[-1]:
                    stack.pop(-1)
                else:
                    stack.append(ch)
            else:
                stack.append(ch)
            print(ch, stack)
        return len(stack)==0
        