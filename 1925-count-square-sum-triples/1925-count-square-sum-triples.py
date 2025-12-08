class Solution:
    def countTriples(self, n: int) -> int:
        ans=[]
        res=[]
        for i in range(1,n+1):
            ans.append(i*i)
        c=0
        for i in range(1,n+1):
            for j in range(1,n+1):
                r=((i*i)+(j*j))
                if r<=n*n:
                    res.append(r)
        print(ans)
        print(res)
        for i in res:
            if i in ans:
                c=c+1
        return c


        