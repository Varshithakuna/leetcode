class Solution:
    def minimumFlips(self, n: int) -> int:
        s=bin(n)[2:]
        k=s[::-1]
        k=list(k)
        s=list(s)

        c=0
        for i in range(len(k)):
            if k[i]!=s[i]:
                c=c+1
        return c
        