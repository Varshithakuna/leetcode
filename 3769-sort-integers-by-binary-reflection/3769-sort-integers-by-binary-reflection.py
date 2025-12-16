class Solution:
    def sortByReflection(self, nums: List[int]) -> List[int]:
        m=[]
        for i in nums:
            h=bin(i)[2::]
            h=list(h)
            h=h[::-1]
            h=''.join(h)
            n=int(h,2)
            m.append([i,n])
        print(m)
        r=sorted(m,key=lambda x:x[1])
        print(r)
        if len(r)==1:
            return [r[0][0]]
        n={}
        for i in r:
            if i[1] not in n:
                n[i[1]]=[]
            n[i[1]].append(i[0])
        ans=[]
        for i in n.values():
            print(i)
            i=sorted(i)
            for j in i:
                ans.append(j)
        return ans
       

        