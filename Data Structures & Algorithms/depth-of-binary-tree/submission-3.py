# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.max = 1
        self.cur = 1

    def maxDepth(self, root: Optional[TreeNode]) -> int:

        if not root:
            return 0
        
        if root.right:
            self.cur += 1
            self.maxDepth(root.right)
            self.max = max(self.max, self.cur)
            self.cur -= 1
        if root.left:
            self.cur += 1
            self.maxDepth(root.left)
            self.max = max(self.max, self.cur)
            self.cur -= 1
        
        return self.max