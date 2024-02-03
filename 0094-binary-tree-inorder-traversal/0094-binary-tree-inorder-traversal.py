# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        x = []
        
        def inorder( root, x):
            
            if root is None:
                return []
            
            inorder(root.left, x)
            x.append(root.val)
            inorder(root.right, x)
            
            return x
        
        return inorder(root, x)
                
                
        