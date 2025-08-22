class Solution:
    def maxScore(self, s: str) -> int:
        ans=[]
        for i in range(len(s)):
            a=s[:i+1]
            b=s[i+1:]
            print(a)
            print(b)
            if len(a)>0 and len(b)>0:
                k=a.count("0")+b.count("1")
                ans.append(k)
        return max(ans)
        