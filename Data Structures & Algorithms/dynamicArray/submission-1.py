class DynamicArray:
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.arr = [0] * self.capacity

    def get(self, i: int) -> int:
        return self.arr[i]

    def set(self, i: int, n: int) -> None:
        self.arr[i] = n

    def pushback(self, n: int) -> None:
        if self.size == self.capacity:
            self.resize()
        self.arr[self.size] = n
        self.size +=1

    def popback(self) -> int:
        temp = self.arr[self.size - 1]
        del self.arr[self.size - 1]
        self.size -=1
        return temp

    def resize(self) -> None:
        self.capacity *= 2
        temp = [0] * self.capacity
        for i in range(self.size):
            temp[i] = self.arr[i]
        del self.arr
        self.arr = temp

    def getSize(self) -> int:
        return self.size
    
    def getCapacity(self) -> int:
        return self.capacity