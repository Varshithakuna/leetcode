class Solution:
    def countTriples(self, n: int) -> int:
        ans=[]
        for i in range(1,n+1):
            ans.append(i*i)
        print(ans)
        c=0
        for i in range(1,n+1):
            for j in range(1,i+1):
                if (i*i)+(j*j) in ans:
                    c=c+1
        print(c)
        return c+c


        