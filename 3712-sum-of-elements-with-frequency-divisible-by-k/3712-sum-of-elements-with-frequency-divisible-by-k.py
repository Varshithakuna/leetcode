class Solution:
    def sumDivisibleByK(self, nums: List[int], k: int) -> int:
        ans=[]
        for i in nums:
            ans.append(nums.count(i))
        print(ans)
        s=0
        for i in range(len(nums)):
            h=ans[i]
            if h%k==0:
                s=s+nums[i]
        return s


        