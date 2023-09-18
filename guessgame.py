class Unionfind:
    def __init__(self, points):
        self.par = {}
        self.rank = {}
        for i in points:
            self.par[tuple(i)] = tuple(i)
            self.rank[tuple(i)] = 1

    def find(self, node):
        if node == self.par[node]:
            return node
        self.par[node] = self.find(self.par[node])
        return self.par[node]

    def union(self, node1, node2):
        x, y = self.find(node1), self.find(node2)
        if x == y:
            return False
        if self.rank[x] > self.rank[y]:
            self.par[y] = x
            self.rank[x] += self.rank[y]
        else:
            self.par[x] = y
            self.rank[y] += self.rank[x]
        return True