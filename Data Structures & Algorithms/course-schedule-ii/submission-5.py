class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = [[] for _ in range(numCourses)]
        ans = []
        seen = {}
        problem = False
        for a, b in prerequisites:
            adj[b].append(a)
        def dfs(node):
            nonlocal problem
            seen[node] = 1
            for next in adj[node]:
                status = seen.get(next, 0)
                if status == 0:
                    dfs(next)
                elif status == 1:
                    problem = True
            seen[node] = 2
            ans.append(node)
        for course in range(numCourses):
            if course in seen: continue
            dfs(course)
            if problem:
                return []
        return ans[::-1]

        