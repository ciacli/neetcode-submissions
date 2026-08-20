from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def walk(self, node, level, accounted, ans):
        if node is None:
            return 
        
        if accounted.get(level, 0) == 0:
            ans.append(node.val)
            accounted[level] = 1

        self.walk(node.right, level + 1, accounted, ans)
        self.walk(node.left, level + 1, accounted, ans)

        
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        accounted = {}
        self.walk(root, 0, accounted, ans)
        return ans