class Solution:
    def commonChars(self, words: List[str]) -> List[str]:    
        fin=[]
        w=words[0]
        w=list(w)
        ans=[]
        fin=[]
        d=[]
        for j in range(1,len(words)):
            ans.append(words[j])
        for i in w:
            c=0
            for j in range(len(ans)):
                if i in ans[j]:
                    c=c+1
            if c==len(ans):
                d.append(i)
        m=[]
        for i in d:
            for j in range(len(ans)):
                n=min(w.count(i),ans[j].count(i))
                m.append([i,n])
        print(m)
        k1=[]
        k2=[]
        s = sorted(m, key=lambda x: x[1])
        for i in s:
            if i[0] not in k1:
                k1.append(i[0])
                k2.append(i)
        for i in k2:
            for j in range(i[1]):
                fin.append(i[0])
        if len(words)>1:
            return fin
        else:
            return w