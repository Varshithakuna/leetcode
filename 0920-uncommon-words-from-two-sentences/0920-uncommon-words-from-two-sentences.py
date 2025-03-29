class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        ans=[]
        # s1=s1.split(" ")
        # s2=s2.split(" ")
        #     s1=set(s1)
        #     s2=set(s2)
        #     m=list(s1-s2)
        #     m=''.join(m)
        #     n=list(s2-s1)
        #     n=''.join(n)
        #     ans.append(m)
        #     ans.append(n)
        # return ans
        s1=s1.split(" ")
        s2=s2.split(" ")
        l=[]
        m=[]
        for i in s1:
            if s1.count(i)==1 and i not in s2:
                l.append(i)
        for j in  s2:
            if s2.count(j)==1 and j not in s1:
                m.append(j)   
        l=set(l)
        m=set(m)
        n=list(l-m)
        o=list(m-l)
        if len(n)>=1:
            for i in n:
                ans.append(i)
        if len(o)>=1:
            for j in o:
                ans.append(j)
        return ans

