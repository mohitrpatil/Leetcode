# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
     
    def findTilt(self, root: Optional[TreeNode]) -> int:
        self.tt = 0
        
        def cal(root:Optional[TreeNode]):
            if root is None:
                return 0

            left = cal(root.left)
            right = cal(root.right)
            tilt = abs(left - right)
            self.tt += tilt

            return left + right + root.val
        
        cal(root)
        return self.tt
            
        
        
        