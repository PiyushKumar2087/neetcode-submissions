# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr=head
        prev=None

        while curr:
            # Save the next node
            nxt=curr.next
            #reverse the link
            curr.next=prev
            # move prev to next
            prev=curr
            # move next
            curr=nxt

            
        return prev

        