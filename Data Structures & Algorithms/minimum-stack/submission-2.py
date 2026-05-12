class MinStack:

    def __init__(self):
        self.arr = []
        self.min_arr = []

    def push(self, val: int) -> None:
        if len(self.min_arr) > 0:
            self.min_arr.append(min(self.min_arr[-1], val))
            self.arr.append(val)
        else:
            self.arr.append(val)
            self.min_arr.append(val)

    def pop(self) -> None:
        del self.arr[-1]
        del self.min_arr[-1]

    def top(self) -> int:
        return self.arr[-1]

    def getMin(self) -> int:
        return self.min_arr[-1]
