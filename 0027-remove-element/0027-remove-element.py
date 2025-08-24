class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        l=0
        r=len(nums)
        d=[]
        for i in range(len(nums)):
            if nums[i]==val:
                l=l+1
            else:
                nums[i-l]=nums[i]
        return r-l
       
        
        

        