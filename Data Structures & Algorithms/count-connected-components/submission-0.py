class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parent = [0] * n
        rank = [0] * n
        ans = n
        def find(node):
            while node != parent[node]:
                parent[node] = parent[parent[node]]
                node = parent[node]
            return node
        for i in range(1, n):
            parent[i] = i
        for ai, bi in edges:
            ra, rb = find(ai), find(bi)
            if ra == rb: continue
            ans -= 1
            if rank[ra] > rank[rb]:
                parent[rb] = ra
            else:
                parent[ra] = rb
                if rank[ra] == rank[rb]:
                    rank[rb] += 1
        return ans