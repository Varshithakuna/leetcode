class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            b=nums[:i]
            c=nums[i+1:]
            if sum(b)==sum(c):
                return i
        else:
            return -1
        