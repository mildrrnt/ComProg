class piggybank:
    def __init__(self):
        self.coins = {}

    def add(self,v,n):
        if sum(self.coins.values()) + n > 100:
            return False
        v = float(v)
        if v not in self.coins:
            self.coins[v] = 0
        self.coins[v] += n
        return True
    
    def __float__(self):
        value = 0.0
        for v in self.coins.keys():
            value += v*self.coins[v]
        return value
    
    def __str__(self):
        return '{'+', '.join('{}:{}'.format(v,self.coins[v]) for v in sorted(self.coins.keys()))+'}'
    
cmd1 = input().split(';') 
cmd2 = input().split(';') 
p1 = piggybank(); p2 = piggybank() 
for c in cmd1: eval(c) 
for c in cmd2: eval(c)