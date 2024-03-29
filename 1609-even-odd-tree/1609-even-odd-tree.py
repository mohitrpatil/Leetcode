# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return False

        level = 0
        evenOddLevel = {0:1, 1:0}
        queue = deque([root])

        while queue:
            prev = 0
            for _ in range(len(queue)):
                currNode = queue.popleft()
                comparison = {0:prev < currNode.val, 1:prev > currNode.val}
                if currNode.val % 2 != evenOddLevel[level % 2]:
                    return False
                else:
                    if prev != 0 and comparison[level % 2]:
                        prev = currNode.val
                    elif prev == 0:
                        prev = currNode.val
                    else:
                        return False

                if currNode.left:
                    queue.append(currNode.left)

                if currNode.right:
                    queue.append(currNode.right)

            level += 1

        return True
        