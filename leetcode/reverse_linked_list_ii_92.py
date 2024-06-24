''' Reverse linked list sublist '''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        # search for left node
        pos = 1
        prev = None
        curr = head
        while pos < left:
            prev = curr
            curr = curr.next
            pos += 1
        
        # record "left" prior node and node at position "left"
        left_prev = prev
        left_pointer = curr
        prev = curr
        curr = curr.next
        pos += 1

        # reverse nodes
        while pos <= right:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next

            pos += 1

        # curr now points to the node after right, and prev points to node at "right"
        if left_prev:
            left_prev.next = prev
        else:
            head = prev
        left_pointer.next = curr
        
        # if we've reversed the head, 
        return head

        