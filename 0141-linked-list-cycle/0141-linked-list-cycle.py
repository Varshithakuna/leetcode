# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        Front = head
        Back = head
        while Back and Back.next:
            Front=Front.next
            Back=Back.next.next
            if Front==Back:
                return True
            
        else:
            return False