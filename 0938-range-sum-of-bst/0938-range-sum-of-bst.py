# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        def cal(root):
            if root is None:
                return 0
             
            val = 0
            if root.val>= low and root.val<=high:
                val = root.val

            left_sum = cal(root.left)
            right_sum =  cal(root.right)

            return val+left_sum+right_sum
  
                
        return cal(root)