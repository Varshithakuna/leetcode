class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        nums=sorted(nums)
        ans=[]
        pans=[]
        for i in range(len(nums)):
            if nums[i]%2==0:
                ans.append(nums[i])
            elif nums[i]%2!=0:
                pans.append(nums[i])
        fin=[]
        for i,j in zip(ans,pans):
            fin.append(i)
            fin.append(j)
        return fin

        

        