class Solution:
    def minOperations(self, nums: List[int]) -> int:
        c=0
        h=nums.copy()
        for i in range(len(nums)-1):
            if nums[i]<nums[i+1]:
                c=c+0
            else:
                k=nums[i]+1
                n=abs(nums[i+1]-k)
                nums[i+1]=k
                c=c+n
        return c
        
        