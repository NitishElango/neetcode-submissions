class TimeMap:

    def __init__(self):
        self.store = dict()

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = [(value, timestamp)]
        else:
            self.store[key].append((value, timestamp))
    
    def get(self, key: str, timestamp: int) -> str:
        res = ""
        if key not in self.store:
            return res
        else:
            l,r = 0, len(self.store[key])-1
            arr = self.store[key]
            while l <= r:
                mid = (l + r) // 2
                if arr[mid][1] <= timestamp:
                    l = mid + 1
                    res = arr[mid][0]
                else:
                    r = mid - 1
            return res