# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        queue = deque([root])
        while queue:
            n = len(queue)
            for _ in range(n):
                node = queue.popleft()
                if node:
                    temp = node.right
                    node.right = node.left
                    node.left = temp
                    if node.right:
                        queue.append(node.right)
                    if node.left:
                        queue.append(node.left)
        
        return root