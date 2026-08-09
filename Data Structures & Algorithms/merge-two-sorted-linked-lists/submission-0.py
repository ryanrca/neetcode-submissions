# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        if list1 == None:
            return list2
        if list2 == None:
            return list1

        # make a new list
        ret = ListNode()

        cur1 = list1
        cur2 = list2
        newList = ret

        while cur1 and cur2:
            # find smalest
            if cur1.val <= cur2.val:
                newList.next = cur1
                cur1 = cur1.next
            else:
                newList.next = cur2
                cur2 = cur2.next
                
            newList = newList.next
            
        # one or both of these are none, append the rest:
        if cur1 is None:
            if cur2:
                newList.next = cur2
        else:
            newList.next = cur1

        # ret.next will drop the first dummy node:
        return ret.next
