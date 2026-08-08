# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        curA = headA
        curB = headB

        while True:

            if curA == curB:
                return curA
        
            if curA == None:
                curA = headB
            else:
                curA = curA.next

            if curB == None:
                curB = headA
            else:
                curB = curB.next

            if curB == None and curA == None:
                return None
