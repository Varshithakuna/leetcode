class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        ans=[]
        ans1=[]
        res=[]
        for i in range(len(nums)):
            k=nums[:i]
            h=nums[i+1::]
            if len(k)>0:
                ans.append(sum(k))
            if len(h)>0:
                ans1.append(sum(h))
            if len(k)==0:
                ans.append(0)
            if len(h)==0:
                ans1.append(0)
        print(ans)
        print(ans1)
        for i in range(len(ans)):
            res.append(abs(ans[i]-ans1[i]))
        return res



        
    
                

                


            


        