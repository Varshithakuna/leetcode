class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        ans=[]
        t=list(t)
        for i in t:
            if i in s:
                ans.append(i)
        left = 0
        h=0
        right = len(ans)
        c=0
        while left<right:
            if s[h]==ans[left] and  h<len(s):
                h=h+1
                c=c+1
                left=left+1
            else :
                left =left+1
        if c==len(s):
            return True
        else:
            return False








