# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:

        def solve(root):

            if root is None:
                return 0
            
            left_sum =  solve(root.left)
            right_sum =  solve(root.right)

            if root.left is None and root.right is None:
                return 1

            if root.left is None:
                return 1+ right_sum
            
            if root.right is None:
                return 1+left_sum
            
            return min(left_sum, right_sum)+1

        x = solve(root)
        
        return x