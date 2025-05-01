class Solution:
    def checkAlmostEquivalent(self, word1: str, word2: str) -> bool:
        s=[]
        k=[]
        for i in word1:
            if i not in s:
                s.append(i)
        for i in word2:
            if i not in k:
                k.append(i)
        ans=0
        ans2=0
        print(k)
        print(s)
        for i in s:
            m=word1.count(i)
            n=word2.count(i)
            if (m-n)<=3:
                ans=ans+1
            else:
                return  False
        for  i in k:
            m =word1.count(i)
            n=word2.count(i)
            if abs(m-n)<=3:
                ans2=ans2+1
            else:
                return False
        if ans2 and ans>0:
            return True
        else:
            return False

        