class Solution:
    def minDeletionSize(self, s: List[str]) -> int:
        c=[]
        for i in range(len(s[0])):
            k=[]
            for j in s:
                k.append(j[i])
            c.append(k)
        ans=0
        for i in c:
            if i==sorted(i):
                continue
            ans=ans+1
        return ans
            