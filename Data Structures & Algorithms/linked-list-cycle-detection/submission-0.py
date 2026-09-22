# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head:
            # This shoul be the brute force way of doing it
            # where we have a seen dictionary that will add 
            # up to the most O(n) space and time is O(n)
            seen = {} #O(n)
            count = 1
            curr = head.next
            while curr:
                if curr in seen.values():
                    return True
                else:
                    seen[count] = curr
                    curr = curr.next
                    count += 1
        return False




        