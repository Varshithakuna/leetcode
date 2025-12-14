class Solution:
    def reverseWords(self, s: str) -> str:
        s=s.split(" ")
        print(s)
        def rev(i):
            h="aeiou"
            k=list(i)
            c=0
            for i in range(len(k)):
                if k[i] in h:
                    c=c+1
            return c
        fin=[]
        m=[]
        for i in s:
            res=rev(i)
            m.append(res)
            fin.append(i)
        for i in range(1,len(m)):
            if m[0]==m[i]:
                u=list(fin[i])
                u=u[::-1]
                u=''.join(u)
                fin[i]=u
        print(fin)
        ans=""
        for i in range(len(fin)-1):
            ans=ans+fin[i]+" " 
        ans=ans+fin[-1]
        return  ans         

        