# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # traverse tree 1
        # compare root.val with tree 2
        # if they are the same, compare trees.
        # continue until you traverse ALL of tree 1's nodes, because there may be other roots that match the sub-tree

        subtrees_match = False

        def trees_match(r1, r2):


            if not r1 and not r2:
                return True

            if r1 and not r2:
                return False

            if r2 and not r1:
                return False

            if r2.val != r1.val:
                return False
            
            left_matches = trees_match(r1.left, r2.left)
            right_matches = trees_match(r1.right, r2.right)

            return left_matches == True and right_matches == True

        def find_same_vals(main, subtree_val):

            nonlocal subtrees_match

            if not main:
                return False

            if main.val == subtree_val:
                if trees_match(main, subRoot):
                    subtrees_match = True
            
            find_same_vals(main.left, subtree_val)
            find_same_vals(main.right, subtree_val)

        find_same_vals(root, subRoot.val)
        return subtrees_match

