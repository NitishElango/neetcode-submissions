class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        t,b = 0, len(matrix) - 1
        while t <= b:
            mid = (t + b)//2
            if matrix[mid][-1] < target:
                t = mid + 1
            elif matrix[mid][-1] > target:
                b = mid - 1
            else:
                return True
        if t < len(matrix) and matrix[t][-1] > target:
            row = t
        else:
            row = b
        
        l,r = 0, len(matrix[0]) - 1
        while l <= r:
            mid = (l+r)//2
            if matrix[row][mid] > target:
                r = mid - 1
            elif matrix[row][mid] < target:
                l = mid + 1
            else:
                return True
        return False
        