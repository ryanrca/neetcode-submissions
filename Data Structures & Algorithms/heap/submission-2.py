class MinHeap:
    
    def __init__(self):
        self.heap = [0] # the first item is a dummy node
        

    def push(self, val: int) -> None:
        self.heap.append(val)
        self._bubble_up(len(self.heap)-1)


    def pop(self) -> int:
        if len(self.heap) < 2:
            return -1
        if len(self.heap) == 2:
            return self.heap.pop()

        result = self.heap[1]
        self.heap[1] = self.heap.pop()
        self._bubble_down(1)
        return result
        

    def top(self) -> int:
        if len(self.heap) < 2:
            return -1

        return self.heap[1]
        

    def heapify(self, nums: List[int]) -> None:
        self.heap = [0] + nums

        # trick: only need to start at 1/2 way through heap
        cursor = (len(self.heap) - 1) // 2
        while cursor >= 1:
            self._bubble_down(cursor)
            cursor -= 1
 

    def heapifyOld(self, nums: List[int]) -> None:
        self.heap = [0] + nums

        # trick: only need to start at 1/2 way through heap
        cursor = (len(self.heap) - 1) // 2
        while cursor >= 1:
            # if there is a r child, then we have 2 children
            if len(self.heap) - 1 >= (cursor * 2) + 1:
                left_val = self.heap[cursor * 2]
                right_val = self.heap[(cursor * 2) + 1]
                # if they are both less then cursor:
                if left_val < self.heap[cursor] and right_val < self.heap[cursor]:
                    # pick smallest and swap
                    if left_val < right_val:
                        self._swap_left_child(cursor)
                    else:
                        self._swap_right_child(cursor)
                # if right is smaller swap R
                elif right_val < self.heap[cursor]:
                    self._swap_right_child(cursor)
                # if L is smaller swap L
                elif left_val < self.heap[cursor]:
                    self._swap_left_child(cursor)

            # if there is a L only, and it's smaller then cursor
                # swap L
            elif len(self.heap) - 1 >= cursor * 2:
                if self.heap[cursor * 2] < self.heap[cursor]:
                    self._swap_left_child(cursor)

            cursor -= 1
        

    def _bubble_up(self, index: int) -> None:
        parent = index // 2

        while self.heap[index] < self.heap[parent]:
            if parent == 0:
                break
            tmp = self.heap[parent]
            self.heap[parent] = self.heap[index]
            self.heap[index] = tmp
            index = parent
            parent = index // 2


    def _swap_left_child(self, parent: int) -> None:
        child = parent * 2
        tmp = self.heap[child]
        self.heap[child] = self.heap[parent]
        self.heap[parent] = tmp

    def _swap_right_child(self, parent: int) -> None:
        child = (parent * 2) + 1
        tmp = self.heap[child]
        self.heap[child] = self.heap[parent]
        self.heap[parent] = tmp

    def _bubble_down(self, index: int) -> None:
        if len(self.heap) <= 2:
            return

        # while we are still in the heap
        while index * 2 < len(self.heap):

            # if we have a right child node, then we have 2 children. 
            length = len(self.heap) - 1
            if length >= (index * 2) + 1:
                left_val = self.heap[(index * 2)]
                right_val = self.heap[(index * 2) + 1]

                # if they are both smaller than parent, swap the smallest:
                if left_val < self.heap[index] and right_val < self.heap[index]:
                    if left_val < right_val:
                        self._swap_left_child(index)
                        index = (index * 2)
                    else:
                        self._swap_right_child(index)
                        index = (index * 2) + 1

                # if right is smaller than parent:
                elif right_val < self.heap[index]:
                    self._swap_right_child(index)
                    index = (index * 2) + 1

                # if left is smaller than parent:
                elif left_val < self.heap[index]:
                    self._swap_left_child(index)
                    index = (index * 2)

                # If both children are larger then current node, we are done.
                if left_val > self.heap[index] and right_val > self.heap[index]:
                    break

            # If we don't have a right child, pick the left node.
            elif self.heap[index * 2] < self.heap[index]:
                self._swap_left_child(index)
                index = (index * 2)
            else:
                break
