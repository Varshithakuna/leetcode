class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        ans=[]
        fin=[]
        for i in range(len(l)):
            s=nums[l[i]:r[i]+1]
            ans.append(s)
        for i in ans:
            p=sorted(i)
            a=[]
            for j in range(len(p)-1):
                a.append(abs((p[j])-(p[j+1])))
            a=set(a)
            print(a)
            if len(a)==1:
                fin.append(True)
            else:
                fin.append(False)
        return fin

            

                
        