# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
    def __eq__(self, other: TreeNode) -> bool:
        if other is None:
            return False
        if not isinstance(other, TreeNode):
            return NotImplemented
        return self.val == other.val


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        left_queue  = deque([p])
        right_queue = deque([q])

        while left_queue and right_queue:
            if len(left_queue) != len(right_queue):
                return False
            for _ in range(len(left_queue)):
                left_node  = left_queue.popleft()
                right_node = right_queue.popleft()

                if left_node != right_node:
                    return False
                
                if left_node:
                    left_queue.append(left_node.left)
                    left_queue.append(left_node.right)
                if right_node:
                    right_queue.append(right_node.left)
                    right_queue.append(right_node.right)
        return True

