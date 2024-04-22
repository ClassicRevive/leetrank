# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    ''' linked list problem where we traverse while making position dependent changes '''
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:     
        curr = head
        # edge cases
        if curr is None:
            return None
        if curr.next is None:
            return curr
        
        even_head = curr.next  # save the head of the even group
        # use leaps of 2 steps to disconnect odd and even nodes
        odd = True
        while curr is not None:
            next_1step = curr.next
            
            if curr.next is not None:
                curr.next = curr.next.next

            if odd:
                odd_tail = curr

            odd = not odd
            curr = next_1step
        
        # append the even group to the odd group
        odd_tail.next = even_head 

        return head


        