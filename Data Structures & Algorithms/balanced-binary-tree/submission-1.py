# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        balanced = True
        
        def is_balanced(root):
            if not root:
                return 0

            nonlocal balanced

            left_depth = is_balanced(root.left)
            right_depth = is_balanced(root.right)

            if abs(left_depth - right_depth) > 1:
                balanced = False

            return 1 + max(left_depth, right_depth)

        is_balanced(root)

        return balanced
