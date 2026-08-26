class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = [[] for _ in range(numCourses)]
        times = [0] * numCourses
        time = 0
        seen = {}
        forward = {}
        for a, b in prerequisites:
            adj[b].append(a)
        def dfs(node):
            nonlocal time
            if node in seen:
                return 
            seen[node] = 1
            for next in adj[node]:
                if next not in seen:
                    forward[(next, node)] = 1
                    dfs(next)
            times[node] = (time, node)
            time = time + 1

        for course in range(numCourses):
            if course in seen: continue
            dfs(course)
        order = sorted(times, key = lambda t: -t[0])
        ans = []
        for _, el in order:
            ans.append(el)
        #print(times)
        #print(forward)
        for a, b in prerequisites:
            if times[b][0] < times[a][0]:
                return []
        return ans

        