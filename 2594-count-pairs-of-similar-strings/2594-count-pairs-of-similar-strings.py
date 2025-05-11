class Solution:
    def similarPairs(self, words: List[str]) -> int:
        p=[]
        c=0
        for i in words:
            s=[]
            for j in range(len(i)):
                s.append(i[j])
            p.append(s)
        for i in range(len(p)):
            for j in range(i+1,len(p)):
                m=p[i]
                n=p[j]
                m=set(m)
                n=set(n)
                m=list(m)
                n=list(n)
                m=sorted(m)
                n=sorted(n)
                if m==n:
                    c=c+1
        return c
        

                


        