# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        self.c=0
        """Function to check if any permutation of self.d in pallindromic"""
        def ispallindrome(d):
            k=0
            for i in d.values():
                if i%2==1:
                    k+=1
                if k>1:
                    return False
            return True
        
        def dfs(root,d):
            if root:
                d[root.val]+=1
                if not root.left and not root.right:
                    if ispallindrome(d):
                        self.c+=1
                dfs(root.left,d)
                dfs(root.right,d)
                d[root.val]-=1
            return
        
        dfs(root,defaultdict(int))
        return self.c
