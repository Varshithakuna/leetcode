# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        arr=[]
        temp=head
        while temp:
            arr.append(temp.val)
            temp=temp.next
        arr=arr[::-1]
        if not arr:
            return 
        head = ListNode(arr[0])
        temp=head
        for i in range(1,len(arr)):
            temp.next=ListNode(arr[i])
            temp=temp.next
        return head

        