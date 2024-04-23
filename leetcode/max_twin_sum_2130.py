# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        # as we move throught the link linked list, store the values in a list
        # we can do this in O(n) time in this way, but the space requirement is also O(n)
        # or we can do this in a memoryless fashion, which is O(n^2) time, but O(1) space

        lst = []
        curr = head
        while curr is not None:
            lst.append(curr.val)

            curr = curr.next 
        
        max_sum = 0
        for i in range(len(lst)//2):
            max_sum = max(max_sum, lst[i] + lst[-i-1])
        
        return max_sum