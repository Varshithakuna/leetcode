class Solution:
    def countTriples(self, n: int) -> int:
        ans=0
        for i in range(1,n+1):
            for j in range(2,n+1):
                for k in range(j,n+1):
                    if ((j*j)+(i*i)==(k*k)):
                        ans=ans+1
        return ans

        