class Solution:
    def minMoves(self, nums: List[int]) -> int:
        n=max(nums)
        h=0
        c=0
        for i in range(len(nums)):
            while nums[i]<n:
                nums[i]=nums[i]+1
                c=c+1
        print(c)
        return c
        