class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Create a hashmap and store each number we iterate through
        set1 = set(nums)
        count = 0
        max_count = 0
        for num in nums:
            while num - count in set1:
                count+=1
            max_count = max(count, max_count)
            count = 1
        return max_count