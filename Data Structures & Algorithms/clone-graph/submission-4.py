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
            if root.val in d:
                return d[root.val]
            
            d.setdefault(root.val, Node(val = root.val, neighbors = []))
            copy = d[root.val]

            for neighbor in root.neighbors:
                neighbor_copy = dfs(neighbor)
                copy.neighbors.append(neighbor_copy) 
                
            return copy
        dfs(node)
        return d[node.val]
                