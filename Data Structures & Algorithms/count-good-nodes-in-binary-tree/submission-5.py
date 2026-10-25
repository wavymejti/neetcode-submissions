# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.output = 0
        rootVal = root.val
        def dfs(node, maxVal):
            if not node:
                return None
            if node.val >= maxVal:
                self.output += 1
            maxVal = max(maxVal, node.val)
            dfs(node.left, maxVal)
            dfs(node.right, maxVal)
        dfs(root, rootVal)
        return self.output