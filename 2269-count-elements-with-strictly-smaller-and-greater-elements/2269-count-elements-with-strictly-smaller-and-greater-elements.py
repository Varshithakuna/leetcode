class Solution:
    def countElements(self, nums: List[int]) -> int:
        c=0
        if len(nums)>1:
            for i in range(len(nums)):
                temp=nums[i+1::]
                semp=nums[:i:]
                ans=temp+semp
                h=min(ans)
                k=max(ans)
                if nums[i]>h and nums[i]<k:
                    c=c+1
        return c
        
        