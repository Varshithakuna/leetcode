class Solution:
    def distinctDifferenceArray(self, nums: List[int]) -> List[int]:
        n=len(nums)
        ans=[]
        for i in range(len(nums)):
            p=nums[:i+1]
            p=set(p)
            s=nums[i+1:]
            s=set(s)
            ans.append(len(p)-len(s))
        return ans

        