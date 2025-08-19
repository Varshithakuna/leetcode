class Solution:
    def maxFreqSum(self, s: str) -> int:
        p="aeiou"
        v=0
        c=0
        for i in s:
            d=s.count(i)
            if i in p:
                v=max(d,v)
            else:
                c=max(c,d)
        return c+v
                

        