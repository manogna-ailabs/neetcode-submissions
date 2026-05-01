class StockSpanner:

    def __init__(self):
        self.stocks = []
        # self.stack = []
        # self.res = []
        self.n = 0
        

    def next(self, price: int) -> int:
        self.stocks.append(price)
        self.n += 1
        
        n = self.n
        while n >0 and self.stocks[n-1] <= price:
            n -= 1
        return self.n - n


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)