# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        def solve(p, q):

            if (p!=None and q ==None) or (p==None and q!=None):
                return False

            if p!= None and q!=None:
                return (p.val == q.val and solve(p.left,q.left) and solve(p.right, q.right))
            
            if p == None and q == None:
                return True
            
        
        return solve(p, q)
        