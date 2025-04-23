class Solution:
    def largestGoodInteger(self, num: str) -> str:
        ans=[]
        p=[]
        s=0
        if len(num)<3:
            return ""
        for i in range(0,len(num)):
            ans.append(num[i:i+3])
        for i in ans:
            m=list(i)
            k=set(m)
            if len(k)==1 and len(m)==3 :
                p.append(i)
        if len(p)<=0:
            return ""
        for i in p:
            i=int(i)
            if s<i:
                s=i
        if s==0:
            s=str(s)
            v= [s]*3
            return ''.join(v)
        return str(s)


            