class Solution:
    def minSwaps(self, s: str) -> int:
        s=list(s)
        c=0
        ans=[]
        for i in s:
            if i=="[":
                ans.append(i)
            else:
                if ans:
                    ans.pop()
                else:
                    c=c+1
                    ans.append(i)
        return c

        