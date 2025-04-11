class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        c=0
        p=[]
        ans=[]
        for i in range(low,high+1):
            i=str(i)
            if len(i)%2==0:
                ans.append(i)
        for i in ans:
            m=i
            z=0
            a=0
            n=(m[:len(m)//2])
            q=m[len(m)//2:len(m)]
            for i in n:
                i=int(i)
                z=z+i
            for i in q:
                i=int(i)
                a=a+i
            if z==a:
                p.append(m)
        return len(p)

        