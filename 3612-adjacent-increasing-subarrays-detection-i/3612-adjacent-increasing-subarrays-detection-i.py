class Solution:
    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
        ans=[]
        for i in range(len(nums)):
            h=nums[i:i+k:]
            if h==sorted(h) and len(set(h))==len(h) and len(h)==k:
                ans.append(i)
        print(ans)
        for i in ans:
            if i+k in ans:
                return True
        else:
            return False
        