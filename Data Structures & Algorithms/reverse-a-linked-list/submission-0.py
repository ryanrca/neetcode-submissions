# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:


        if head is None: 
            print(head)
            print(head)
            print(head)

            return None 

        left = None

        cur = head

        while cur:
            tmp = cur.next
            cur.next = left
            left = cur
            cur = tmp

        head = left
        return head

        
