# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        if p is None and q is None:
            return True

        def are_bst_same(r1, r2):

            if not r1 and not r2:
                return True

            if r1 and not r2:
                return False

            if r2 and not r1:
                return False

            if r1.val != r2.val:
                return False

            left_tree = are_bst_same(r1.left, r2.left)
            right_tree = are_bst_same(r1.right, r2.right)

            return left_tree and right_tree

        same = are_bst_same(p, q)

        return same
