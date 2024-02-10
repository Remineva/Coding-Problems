class UF:
    def __init__(self, n):
        self.root = [i for i in range(n)]
        self.rank = [1] * n
    
    def find(self, x):
        t = x
        while self.root[x] != x:
            x = self.root[x]
        while t != x:
            t, self.root[t] = self.root[t], x
        return x
    
    def union(self, x, y):
        X = self.find(x)
        Y = self.find(y)
        if X != Y:
            if self.rank[X] > self.rank[Y]:
                self.root[Y] = X
            elif self.rank[X] < self.rank[Y]:
                self.root[X] = Y
            else:
                self.root[X] = Y
                self.rank[Y] += 1