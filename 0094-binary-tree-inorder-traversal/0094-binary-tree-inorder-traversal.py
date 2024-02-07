# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        
        def solve(root, ans):
            
            if root is None:
                return []
            
            solve(root.left, ans)
            ans.append(root.val)
            solve(root.right, ans)
            
            return ans
        
        ans = solve(root, ans)
        return ans
                
                
        