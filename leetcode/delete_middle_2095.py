# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # find the length of the linked list
        curr = head
        size = 0
        while curr is not None:
            size += 1
            curr = curr.next
        
        
        middle = size//2
        if middle==0:
            return None
        curr = head
        # go to the node right before the middle and skip the middle
        for i in range(middle-1):
            curr = curr.next
        curr.next = curr.next.next

        return head

        
        