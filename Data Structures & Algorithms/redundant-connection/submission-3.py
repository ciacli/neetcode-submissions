class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        stcc = {}
        cnt = 1
        ans = []
        for ai, bi in edges:
            if ai not in stcc and bi not in stcc:
                stcc[ai], stcc[bi] = cnt, cnt
                cnt += 1
            elif bi not in stcc:
                stcc[bi] = stcc[ai]
            elif ai not in stcc:
                stcc[ai] = stcc[bi]
            else:
                if stcc[ai] == stcc[bi]:
                    ans = [ai, bi]
                else:
                    old = stcc[bi]
                    for node in stcc:
                        if stcc[node] == old:
                            stcc[node] = stcc[ai]
                
        return ans