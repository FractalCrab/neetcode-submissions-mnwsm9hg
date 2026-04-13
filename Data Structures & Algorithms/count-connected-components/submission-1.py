class UnionFind:
     def __init__(self, size):
         self.parents = [node for node in range(size)]
     
     def union(self, i, j):
         i_rep = self.find(i)
         j_rep = self.find(j)

         self.parents[j_rep] = i_rep

     def find(self, i):
         if self.parents[i] == i:
            return i
         
         return self.find(self.parents[i])

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        uf = UnionFind(n)
        connected = 0
        for u, v in edges:
            uf.union(u, v)
        
        return sum(1 for i in range(n) if uf.find(i) == i)