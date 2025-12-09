class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        for i in nums:
            if (2*nums.count(i)==len(nums)):
                return i
        