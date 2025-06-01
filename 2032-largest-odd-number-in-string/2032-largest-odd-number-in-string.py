class Solution:
    def largestOddNumber(self, num: str) -> str:
        ans=[]
        p=[]
        for i in range(len(num)-1,-1,-1):
            m=num[i]
            m = int(m)
            if m%2!=0:
                n=(num[:i+1])
                p.append(n)
                break
        print(p)
        if len(p)>0:
            return (p[0])
        else:
            return ''



        