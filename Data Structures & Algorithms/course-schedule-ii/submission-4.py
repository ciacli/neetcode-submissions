class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = [[] for _ in range(numCourses)]
        times = [0] * numCourses
        time = 0
        seen = {}
        problem = False
        for a, b in prerequisites:
            adj[b].append(a)
        def dfs(node):
            nonlocal time
            nonlocal problem
            seen[node] = 1
            for next in adj[node]:
                status = seen.get(next, 0)
                if status == 0:
                    dfs(next)
                elif status == 1:
                    problem = True
            seen[node] = 2
            times[node] = (time, node)
            time = time + 1

        for course in range(numCourses):
            if course in seen: continue
            dfs(course)
            if problem:
                return []
        times = sorted(times, key = lambda t: -t[0])
        ans = []
        for _, el in times:
            ans.append(el)
        return ans

        