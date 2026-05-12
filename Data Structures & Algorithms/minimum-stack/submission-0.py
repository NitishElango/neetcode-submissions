class MinStack:

    def __init__(self):
        self.arr = []

    def push(self, val: int) -> None:
        self.arr.append(val)

    def pop(self) -> None:
        del self.arr[-1]

    def top(self) -> int:
        return self.arr[-1]
              
    def getMin(self) -> int:
        min1 = self.arr[0]
        for num in self.arr:
            if num < min1:
                min1 = num
        return min1
