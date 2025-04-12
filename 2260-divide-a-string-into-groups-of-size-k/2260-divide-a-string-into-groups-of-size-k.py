class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        a=[]
        for i in range(0,len(s),k):
            a.append(s[i:i+k])
        m=a[-1]
        if len(m)!=k:
            q=k-len(m)
            r=m+""
            for i in range(q):
                r=r+fill
            a.pop(len(a)-1)
            a.append(r)
        

        return a
            

        
        