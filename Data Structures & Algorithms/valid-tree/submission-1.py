class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        ans = True
        parent = [0] * (n + 1)
        rank = [0] * (n + 1)
        for i in range(n):
            parent[i] = i
        def find(node):
            while node != parent[node]:
                parent[node] = parent[parent[node]]
                node = parent[node]
            return node
        for ai, bi in edges:
            ra, rb = find(ai), find(bi)
            if ra == rb:
                return False
            if rank[ra] > rank[rb]:
                parent[rb] = ra
            else:
                parent[ra] = rb
                if rank[ra] == rank[rb]:
                    rank[rb] += 1
        for i in range(1, n):
            if find(i) != find(i - 1):
                return False
        return True

