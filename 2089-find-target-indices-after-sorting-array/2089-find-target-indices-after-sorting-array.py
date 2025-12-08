class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        ans=[]
        nums = sorted(nums)
        for i in range(len(nums)):
            if nums[i]==target:
                ans.append(i)
        return ans
        