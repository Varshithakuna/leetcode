class Solution:
    def maximumHappinessSum(self, h: List[int], k: int) -> int:
        h=sorted(h)
        c=0
        if len(h)==0:
            return 0
        if len(h)==1:
            c=c+h.pop()
        for i in range(k):
            m=h.pop()
            if m-i>=0:
                c=c+m-i
        return c



        