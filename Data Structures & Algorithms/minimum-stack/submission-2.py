class Node:
    def __init__(self, val = None):
        self.val = val
        self.prev = None
        self.next = None

class MinStack:

    def __init__(self):
        self.count = 0
        self.minvals = []
        self.tail = None
        
    def dump(self):
        cur = self.tail
        while cur is not None:
            print(f" [{cur.val}] -> ", end="")
            cur = cur.prev
        print(f"\n min: {self.minvals[len(self.minvals)-1]} - count: {self.count}")


    def push(self, val: int) -> None:

        new_node = Node(val)

        if self.count == 0:
            self.tail = new_node
            self.minvals.append(val)
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

        cur_minval = self.minvals[len(self.minvals)-1]

        if cur_minval < val:
            self.minvals.append(cur_minval)
        else:
            self.minvals.append(val)
        self.count += 1
        
    def pop(self) -> None:
        if self.count == 0:
            return

        self.minvals.pop()
        
        if self.count == 1:
            self.tail = None
            self.count -= 1
            return
        tmp = self.tail
        self.tail = self.tail.prev
        self.tail.next = None
        self.count -= 1
        

    def top(self) -> int:
        if not self.tail:
            return None
        return self.tail.val
        

    def getMin(self) -> int:
        return self.minvals[len(self.minvals)-1]
        