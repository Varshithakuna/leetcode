class Solution:
    def evenNumberBitwiseORs(self, nums: List[int]) -> int:
        ans=[]
        for i in nums:
            if i%2==0:
                ans.append(i)
        if len(ans)>0:
            c=0
            for i in ans:
                c=c|i
            return c
        return 0


        