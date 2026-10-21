# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        deptLeft = self.maxDepth(root.left)
        deptRight = self.maxDepth(root.right)
        maxDepth = max(deptLeft, deptRight) + 1
        return maxDepth