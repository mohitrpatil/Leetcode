# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        x = []
        y = []
        
        def traverseleaf(root, p):
            
            if root == None:
                return p
            
            if root.left == None and root.right == None:
                p.append(root.val)
            
            else:
                traverseleaf(root.left, p)
                traverseleaf(root.right, p)
                
            return p
    
        x = traverseleaf(root1, x)
        # print(x)
        y = traverseleaf(root2, y)
        # print(y)
        
        if x == y:
            return True
        return False
        
        
            