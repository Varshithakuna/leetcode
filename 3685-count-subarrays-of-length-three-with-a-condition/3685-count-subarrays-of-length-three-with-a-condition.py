class Solution:
    def countSubarrays(self, nums: List[int]) -> int:
        p=[]
        c=0
        for i in range(len(nums)):
            temp=[]
            for j in range(i,len(nums)):
                temp.append(nums[j])
                if len(temp[::])==3:
                    p.append(temp[::])
        for i in p:
            if i[0]+i[2]==(i[1]/2):
                c=c+1
        return c
