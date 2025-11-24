class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        p=[str(nums[0])]
        ans=[]
        for i in range(1,len(nums)):
            v=""
            v=v+p[i-1]+str(nums[i])
            p.append(v)
        for i in p:
            k=int(i,2)
            if k%5==0:
                ans.append(True)
            else:
                ans.append(False)
        return ans
        