from collections import deque

class TreeNode:
    def __init__(self, key = None, val = None):
        self.key = key
        self.val = val
        self.left = None
        self.right = None

class TreeMap:
    
    def __init__(self):
        self.head = None
 
    def find(self, root, key):
        if not root:
            return None

        if root.key == key:
            return root

        if key < root.key:
            return self.find(root.left, key)

        if key > root.key:
            return self.find(root.right, key)

    def insert(self, key: int, val: int) -> None:

        if not self.head:
            self.head = TreeNode(key, val)
            return

        def iinsert(root, key, val):
            if not root:
                return TreeNode(key, val)

            if root.key == key:
                root.val = val
            elif key < root.key:
                root.left = iinsert(root.left, key, val)
            elif key > root.key:
                root.right = iinsert(root.right, key, val)


            return root
        self.head = iinsert(self.head, key, val)
        return
            
    def get(self, key: int) -> int:

        if not self.head:
            return -1
        
        node = self.find(self.head, key)
        if node:
            return node.val
        else:
            return -1

    def getMin(self) -> int:
        if not self.head:
            return -1
        
        cursor = self.head
        while cursor.left:
            cursor = cursor.left

        return cursor.val

    def getMax(self) -> int:
        if not self.head:
            return -1

        cursor = self.head
        while cursor.right:
            cursor = cursor.right
        return cursor.val

    def findMin(self, root: TreeNode) -> TreeNode:
        cursor = root
        while cursor and cursor.left:
            cursor = cursor.left
        return cursor
   
    def remove(self, key: int) -> None:

        def rremove(root, key):
            if not root:
                return None

            if key < root.key:
                root.left = rremove(root.left, key)
            elif key > root.key:
                root.right = rremove(root.right, key)

            else:
                # node has 0 or 1 children
                if not root.right:
                    return root.left
                if not root.left:
                    return root.right
                # node has 2 children
                else:
                    minNode = self.findMin(root.right)
                    root.key = minNode.key
                    root.val = minNode.val
                    root.right = rremove(root.right, minNode.key)
            return root

        self.head = rremove(self.head, key)
           
    def getInorderKeys(self) -> List[int]:
        ret = []
        if not self.head:
            return ret

        def inorder(node, result):
            if not node:
                return
            inorder(node.left, result)
            result.append(node.key)
            inorder(node.right, result)

        inorder(self.head, ret) 
        return ret
