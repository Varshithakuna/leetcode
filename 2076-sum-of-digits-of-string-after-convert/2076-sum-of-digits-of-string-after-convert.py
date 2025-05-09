class Solution:
    def getLucky(self, s: str, k: int) -> int:
        p=""
        ans=0
        for i in s:
            p=p+str(ord(i)-96)
        for j in range(k):
            for i in p:
                i=int(i)
                ans=ans+i
            p=str(ans)
            ans=0
        return int(p)
    