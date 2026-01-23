class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        ans=[nums[0]]
        left =[]
        for i in range(len(nums)):
            if ans:
                if ans[-1]<nums[i]:
                    ans.append(nums[i])
                else:
                    left.append(len(ans))
                    ans=[]
                    ans.append(nums[i])
        left.append(len(ans))
        print(ans)
        print(left)
        return max(left)


        