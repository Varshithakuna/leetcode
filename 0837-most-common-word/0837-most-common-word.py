class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        ans=[]
        d={}
        q=[]
        paragraph=paragraph.split()
        for i in paragraph:
            h=i.split(",")
            if len(i)>2:
                for j in h:
                    if len(j)>0:
                        q.append(j.lower())
            else:
                q.append(i.lower())
        print(q)
                
        p=[]
        for i in banned:
            i=i.lower()
            p.append(i)
        for i in q:
            i=i.lower()
            if i[len(i)-1]==',' or  i[len(i)-1]=='.' or i[len(i)-1]=="!" or i[len(i)-1]=="?" or i[len(i)-1]==";"or i[len(i)-1]=="'":
                k=i[0:len(i)-1]
                if len(banned)>0:
                    if k not in p:
                        ans.append(k)
                else:
                    ans.append(k)
            else:
                if len(banned)>0:
                    if i not in p:
                        ans.append(i.lower())
                else:
                    ans.append(i)
        print(ans)
        for i in ans:
            if i in d:
                d[i]=d[i]+1
            else:
                d[i]=1
        m=0
        for i in d:
            if d[i]>=m:
                m=d[i]
        for i in d:
            if m==d[i]:
                return i.lower()

            
        