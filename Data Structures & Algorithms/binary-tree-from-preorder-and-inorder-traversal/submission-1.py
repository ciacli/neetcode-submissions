# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        root = TreeNode()
        cur = root
        n = len(preorder)
        i = 0
        j = 0
        d = {}
        def dfs(node):
            nonlocal i
            nonlocal j
            node.val = preorder[i] 
            d[node.val] = node
            i += 1
            if i >= n:
                return
            if preorder[i - 1] == inorder[j]:
                j += 1
                while j < n and d.get(inorder[j], None):
                    node = d[inorder[j]]
                    j += 1
                if j == n:
                    return 
                right = TreeNode()
                node.right = right
                dfs(right)
            else:
                left = TreeNode()
                node.left = left
                dfs(left)
               
        dfs(root)
        return root


