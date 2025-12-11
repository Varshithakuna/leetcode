class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        ans=[]
        while nums:
            a=min(nums)
            nums.remove(a)
            b=min(nums)
            nums.remove(b)
            ans.append(b)
            ans.append(a)
        return ans

        