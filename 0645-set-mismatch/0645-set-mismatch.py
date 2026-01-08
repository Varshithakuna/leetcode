class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        ans =[]
        d={}
        for i in nums:
            if i not in d:
                d[i]=1
            else:
                d[i]=d[i]+1
        for i in d:
            if d[i] ==2:
                ans.append(i)
        for i in range(1,len(nums)+1):
            if i not in nums:
                ans.append(i)
        return ans
   
        