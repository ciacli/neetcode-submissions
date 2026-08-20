"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        d = {}
        if not node:
            return None
        def dfs(root):
            
            d.setdefault(root.val, Node(val = root.val, neighbors = []))
            copy = d[root.val]
            for neighbor in root.neighbors:

                if not neighbor.val in d:
                    dfs(neighbor)

                neighbor_copy = d[neighbor.val]
                if neighbor_copy:
                    copy.neighbors.append(neighbor_copy)
        dfs(node)
        return d[node.val]
                