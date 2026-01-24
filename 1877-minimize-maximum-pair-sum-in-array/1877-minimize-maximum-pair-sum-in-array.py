class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        ans=[]
        nums=sorted(nums)
        for i in range(len(nums)):
            k=nums[i]+nums[len(nums)-i-1]
            ans.append(k)
        print(ans)
        return max(ans)
        
        