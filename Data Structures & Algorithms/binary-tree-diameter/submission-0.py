# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        longest_path = 0

        def find_diameter(root):

            nonlocal longest_path

            if not root:
                return 0

            left_length = find_diameter(root.left)
            right_length = find_diameter(root.right)

            length = left_length + right_length

            longest_path = max(length, longest_path)

            return 1 + max(left_length, right_length)


        find_diameter(root)

        return longest_path