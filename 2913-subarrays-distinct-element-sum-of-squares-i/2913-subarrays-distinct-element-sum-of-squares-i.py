class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        arr=[]
        for i in range(len(nums)):
            for j in range(i,len(nums)):
                temp=nums[i:j+1]
                temp=sorted(temp)
                arr.append(temp)
        c=0
        for i in arr:
            s=set(i)
            c=c+len(s)*len(s)
        return c

            
        