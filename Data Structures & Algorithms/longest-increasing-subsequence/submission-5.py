class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        LIS = []
        for num in nums:
            if not LIS or LIS[-1] < num:
                LIS.append(num)
            else:
                    l, r = 0, len(LIS) - 1
                    while l <= r:
                        mid = (l + r) // 2
                        if LIS[mid] < num:
                            l = mid + 1
                        else:
                            r = mid - 1
                    LIS[l] = num
        return len(LIS)