class Solution:
    def getLeastFrequentDigit(self, n: int) -> int:
        s=[]
        n=str(n)
        for i in n:
            i=int(i)
            s.append(i)
        d={}
        for i in s:
            if i not in d:
                d[i]=1
            else:
                d[i]=d[i]+1
        print(d)
        r=sorted(d.values())
        m=min(r)
        ans=[]
        for i in d:
            if d[i]==m:
                ans.append(i)
        return min(ans)
        