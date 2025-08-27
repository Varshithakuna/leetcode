class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums=sorted(nums)
        ans=[]
        for i in range(0,len(nums)-1,2):
            a=[nums[i],nums[i+1]]
            ans.append(a)
        print(ans)
        c=0
        for i in ans:
            c=c+min(i)
        print(ans)
        return c

        
        