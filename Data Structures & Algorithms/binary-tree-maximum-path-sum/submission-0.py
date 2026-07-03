# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        self.max_sum = root.val
        def dfs(node):
            if not node:
                return 0
            
            left_sum  = dfs(node.left)
            right_sum = dfs(node.right)

            left_max = max(0, left_sum)
            right_max = max(0, right_sum)

            self.max_sum = max(self.max_sum, node.val + left_max + right_max)
            return node.val + max(left_max, right_max)
        
        dfs(root)
        return self.max_sum