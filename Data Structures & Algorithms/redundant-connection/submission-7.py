class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        ans = []
        parent = [0] * (n + 1)
        rank = [0] * (n + 1)
        def find(node):
            while parent[node] != node:
                parent[node] = parent[parent[node]]
                node = parent[node]
            return node

        for i in range(1, n + 1):
            parent[i] = i
        #print(parent)
        for ai, bi in edges:
            ra, rb = find(ai), find(bi)
            #ra, rb = ai, bi
            if ra == rb:
                ans = [ai, bi]
                break
            if rank[ra] > rank[rb]:
                parent[rb] = ra
                rank[ra] += 1
            else:
                parent[ra] = rb
                rank[rb] += 1
        return ans