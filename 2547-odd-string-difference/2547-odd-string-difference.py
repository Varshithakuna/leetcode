class Solution:
    def oddString(self, words: List[str]) -> str:
        ans=[]
        for i in words:
            a=[]
            for j in range(len(i)-1):
                a.append(((ord(i[j+1])-97)) - ((ord(i[j]))-97))
            ans.append(a)
        fin = 0
        f=[]
        for i in ans:
            if ans.count(i)==1:
                m=ans.index(i)
                fin=m
                break
        return words[fin]
        


                
        