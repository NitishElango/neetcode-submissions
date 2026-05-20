class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        LIS = []
        for num in nums:
            if not LIS:
                LIS.append(num)
            else:
                if LIS[-1] < num:
                    LIS.append(num)
                else:
                    for i in range(len(LIS)):
                        if LIS[i] >= num:
                            LIS[i] = num
                            break
        return len(LIS)
                    