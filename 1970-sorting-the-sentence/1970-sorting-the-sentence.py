class Solution:
    def sortSentence(self, s: str) -> str:
        s=s.split(" ")
        ans=[]
        p=[]
        for i in s:
            a=(i[-1])   
            a=int(a)
            ans.append(a)  
        for i in s:
            a=i[0:len(i)-1]  
            p.append(a)
        print(p)
        k=["0"]*max(ans)
        print(k)
        for i in range(len(ans)):
            k[ans[i]-1]=p[i]
        print(k)
        l=""
        for i in k:
            l=l+i+" "
        l = l.strip()
        return l

    
        