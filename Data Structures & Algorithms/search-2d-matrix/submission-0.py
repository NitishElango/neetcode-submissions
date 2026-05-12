class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # binary search to find the right row
        # then binary search to find the right element

        t, b =0, len(matrix) - 1

        while t <= b:
            mrow = (t+b)//2
            if target > matrix[mrow][-1]:
                t = mrow + 1
            elif target < matrix[mrow][0]:
                b = mrow - 1
            else:
                break
        row = matrix[mrow]
        l, r = 0, len(row) - 1
        while l <= r:
            mid = (l+r)//2
            print(row[mid], target)
            if row[mid] > target:
                r = mid - 1
            elif row[mid] < target:
                l = mid + 1
            else:
                return True
        return False