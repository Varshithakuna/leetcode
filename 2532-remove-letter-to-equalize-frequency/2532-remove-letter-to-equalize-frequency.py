class Solution:
    def equalFrequency(self, word: str) -> bool:
        w=[]
        for i in word:
            w.append(i)
        if len(w)==len(set(w)):
            return True
        else:
            for i in range(len(w)):
                ans=[]
                m=w[i+1::]
                k=w[:i:]
                m1=m+k
                m2=set(m1)
                m2=list(m2)
                for i in m2:
                    ans.append(m1.count(i))
                if len(set(ans))==1:
                    return True
                    break
            else:
                return False
        
                
        

        