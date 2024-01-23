# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        
        if root.left == None and root.right == None:
            return True
        
        def mirror(l , r):
            if l==None and r==None:
                return True
            if l == None or r == None:
                return False
            if l != None and r != None:
                return ((l.val == r.val) and mirror(l.left, r.right)
                       and mirror(l.right, r.left))
        
        return mirror(root.left, root.right)
        