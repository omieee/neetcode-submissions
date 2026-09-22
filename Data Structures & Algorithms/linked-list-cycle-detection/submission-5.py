# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head:
            sl_ptr = head
            fs_ptr = head.next
            while fs_ptr:
                if sl_ptr == fs_ptr:
                    return True
                else:
                    if fs_ptr.next is None:
                        return False
                    else:
                        sl_ptr = sl_ptr.next
                        fs_ptr = fs_ptr.next.next
        return False
        