# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        #czuje ze to BFS
        if not p and not q:
            return True
        resultL = []
        resultR = []
        queueL = deque([p])
        queueR = deque([q])
        while queueL:
            levelSize = len(queueL)
            currentLevel = []
            for _ in range(levelSize):
                node = queueL.popleft()
                if node is None:
                    currentLevel.append(None)
                else:
                    currentLevel.append(node.val)
                    queueL.append(node.left)
                    queueL.append(node.right)
            resultL.append(currentLevel)
        while queueR:
            levelSize = len(queueR)
            currentLevel = []
            for _ in range(levelSize):
                node = queueR.popleft()
                if node is None:
                    currentLevel.append(None)
                else:
                    currentLevel.append(node.val)
                    queueR.append(node.left)
                    queueR.append(node.right)
            resultR.append(currentLevel)
        if resultL == resultR:
            return True
        else:
            return False
