class Solution:
    def minElement(self, nums: List[int]) -> int:
        ans=[]
        for i in nums:
            k=0
            i=str(i)
            for j in i:
                j = int(j)
                k=k+j
            ans.append(k)
        return min(ans)




        