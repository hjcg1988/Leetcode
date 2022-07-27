# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        current = head
        pal=[]
        while current != None:
            pal.append(current.val)
            current=current.next
        return pal == pal[::-1]
