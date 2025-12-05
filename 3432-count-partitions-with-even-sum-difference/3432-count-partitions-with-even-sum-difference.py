class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        c=0
        for i in range(len(nums)-1):
            a1=nums[i+1::]
            b1=nums[:i+1:]
            s=sum(a1)-sum(b1)
            s=abs(s)
            if s%2==0:
                c=c+1
        return c
        