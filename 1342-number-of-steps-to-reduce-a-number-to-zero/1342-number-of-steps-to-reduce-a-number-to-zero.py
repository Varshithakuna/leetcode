class Solution:
    def numberOfSteps(self, num: int) -> int:
        c=0
        m=num
        while m:
            if m%2==0:
                m=m//2
                c=c+1
            else:
                m=m-1
                c=c+1
        return c
        