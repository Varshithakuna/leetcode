class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        ans=[]
        for i in range(len(nums)):
            if nums[i]==1:
                ans.append(i)
        print(ans)
        for i in range(1,len(ans)):
            if abs(ans[i-1]-ans[i])>k:
                continue
            else:
                return False
        return True

        


        