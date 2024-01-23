# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def traverse(self, root, ind):
        
        if not root:
            return 0
        
        if not root.left and not root.right and ind:
            return root.val
        
        left_sum = self.traverse(root.left, True)
        right_sum = self.traverse(root.right, False)
        
        return left_sum + right_sum

    
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        result = 0
        return self.traverse(root, False)
        
        