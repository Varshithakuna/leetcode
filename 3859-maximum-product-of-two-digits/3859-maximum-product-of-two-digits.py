class Solution:
    def maxProduct(self, n: int) -> int:
        n=str(n)
        s=[]
        for i in n:
            s.append(int(i))
        s=sorted(s)
        return s[-2]*s[-1]
        