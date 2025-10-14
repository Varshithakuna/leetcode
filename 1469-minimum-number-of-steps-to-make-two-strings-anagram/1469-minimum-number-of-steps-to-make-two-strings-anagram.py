class Solution:
    def minSteps(self, s: str, t: str) -> int:
        s=sorted(s)
        t=sorted(t)
        ans=[]
        pans=[]
        for i,j in zip(s,t):
            if i!=j:
                ans.append(i)
                pans.append(j)
        if len(set(s))==1 and len(set(t))==1 and s[0]!=t[0]:
            return len(s)

        for i in ans:
            if i in pans:
                h = pans.index(i)
                pans.pop(h)
        return len(pans)
        