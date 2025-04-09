class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s1=[]
        t1=[]
        for i in s:
            s1.append(i)
        for i in t:
            t1.append(i)
        s1=set(s1)
        s1=list(s1)
        t1=set(t1)
        t1=list(t1)
        m=list(set(zip(s,t)))
        print(m)
        if len(s1)==len(t1)==len(m) :
            return True
        else:
            return False
        
        