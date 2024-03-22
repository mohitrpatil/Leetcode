# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        
        a = []
        
        while head:
            a.append(str(head.val))
            head = head.next

        s =""
        
        for i in a:
            s += i
            
        if s == s[::-1]:
            return True
        else:
            return False