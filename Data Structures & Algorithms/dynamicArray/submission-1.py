class DynamicArray:
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.array = []


    def get(self, i: int) -> int:
        return self.array[i]


    def set(self, i: int, n: int) -> None:
        self.array[i] = n


    def pushback(self, n: int) -> None:
        if self.size >= self.capacity:
            self.resize()
        self.array.append(n)
        self.size += 1

    def popback(self) -> int:
        ret = self.array[len(self.array)-1]
        del(self.array[len(self.array)-1])
        self.size -= 1
        return ret
 

    def resize(self) -> None:
        self.capacity = self.capacity*2


    def getSize(self) -> int:
        return self.size
        
    
    def getCapacity(self) -> int:
        return self.capacity
