class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre = [1 for n in range(len(nums))]
        post = [1 for n in range(len(nums))]
        for i in range(1,len(nums)):
            pre[i] = pre[i-1] * nums[i-1]
        for i in range(len(nums)-2, -1, -1):
            post[i] = post[i+1] * nums[i+1]
        sol = []
        for i in range(len(pre)):
            sol.append(pre[i] * post[i])
        return sol

        