class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        ans=[]
        pans=[]
        res=[]
        for i in range(len(nums)):
            if nums[i]<0:
                pans.append(nums[i])
            else:
                ans.append(nums[i])
        for i,j in zip(ans,pans):
            res.append(i)
            res.append(j)
        print(res)
        return res

     