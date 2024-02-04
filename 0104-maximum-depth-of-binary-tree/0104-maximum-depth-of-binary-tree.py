# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        ans = 0

        def solve(root, ans):

            if root ==None:
                return 0

            ans += 1 + max(solve(root.left, ans), solve(root.right, ans))

            return ans
        
        x = solve(root, ans)
        
        return x
        