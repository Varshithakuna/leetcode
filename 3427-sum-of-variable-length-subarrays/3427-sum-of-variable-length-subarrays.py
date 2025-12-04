class Solution:
    def subarraySum(self, nums: List[int]) -> int:
        ans=[]
        res= []
        fin=0
        for i in range(len(nums)):
            start=max(0,i-nums[i])
            h=[start,i]
            h=set(h)
            h=list(h)
            h=sorted(h)
            ans.append(h)
        print(ans)
        for i in ans:
            k=min(i)
            n=max(i)
            b=nums[k:n+1]
            fin=fin+sum(b)
            res.append(b)
        print(fin)
        return fin
        



            
        

        