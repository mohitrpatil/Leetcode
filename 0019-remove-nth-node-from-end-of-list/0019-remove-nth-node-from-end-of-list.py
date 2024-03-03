# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head == None or head.next == None: return None

        dummy = ListNode(0)
        dummy.next = head
        count = 0

        iterate = head
        while iterate != None:
            count+=1
            iterate = iterate.next 

        count-=n
        prev = dummy
        for i in range(0 , count):
            prev = prev.next

        prev.next = prev.next.next
        return dummy.next
