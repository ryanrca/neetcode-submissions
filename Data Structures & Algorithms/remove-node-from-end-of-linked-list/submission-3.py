# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def dump(self):
        h = head
        while h is not None:
            print(f" [{h.val}] -> ", end="")
            h = h.next
        print(".")

    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        left = head
        right = head
        prev = head

        for j in range(n):
            right = right.next

        while right is not None:
            prev, left = left, left.next
            right = right.next

        # left is the node we need deleted
        # if left is the first item in the list:
        if head == left:
            head = left.next
        else:
            prev.next = left.next

        return head