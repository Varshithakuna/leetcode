class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        nums1=sorted(nums)
        c=0
        ans=[]
        for i in nums1:
            if 2*i<=nums1[-1]:
                ans.append(i)
        print(ans)  
        if len(ans)==len(nums)-1:
            return nums.index(nums1[-1])
        else:
            return -1
        
        


        