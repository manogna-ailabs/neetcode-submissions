class FreqStack:

    def __init__(self):
        self.stack = {}
        self.max_count = 0
        self.count = {}

    def push(self, val: int) -> None:
        self.count[val] = self.count.get(val, 0) + 1
        self.stack[self.count[val]] = self.stack.get(self.count[val], []) + [val]
        self.max_count = max(self.max_count, self.count[val])

    def pop(self) -> int:
        val = self.stack[self.max_count].pop()
        self.count[val] -= 1
        if not self.stack[self.max_count]:
            self.max_count -= 1
        return val
        
        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()