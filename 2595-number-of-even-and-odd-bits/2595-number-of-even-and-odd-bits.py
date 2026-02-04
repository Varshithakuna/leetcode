class Solution:
    def evenOddBit(self, n: int) -> List[int]:
        n=bin(n)[2::]
        n=n[::-1]
        c=[]
        print(n)
        for i in range(len(n)):
            if n[i]=='1':
                c.append(i)
        print(c)
        fin=[]
        m=0
        l=0
        for i in c:
            if i%2==0:
                m=m+1
            else:
                l=l+1
        return [m,l]



        