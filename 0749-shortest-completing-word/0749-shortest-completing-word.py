class Solution:
    def shortestCompletingWord(self, l: str, words: List[str]) -> str:
        q=[]
        ans=[]
        for i in l:
            if i.isalpha():
                p=i.lower()
                q.append(p)
        for i in range(len(words)):
            c=0
            for j in q:
                if q.count(j)<=words[i].count(j):
                    c=c+1
            if c==len(q):
                ans.append(words[i])
        print(ans)
        if len(ans)>1:
            d=[]
            for i in ans:
                d.append(len(i))
            f=min(d)
            k=d.index(f)
            return ans[k]
        else:
            return ''.join(ans)

        


            

        # for i in words:
        #     c=0
        #     for j in range(len(i)):
        #         if i[j] in p:
        #             if i.count(i[j])>=p.count(i[j]):
        #                 c=c+1
        #     if c>=len(p):
        #         if len(ans)==0:
        #             ans.append(i)
        #         if len(ans)>=1:
        #             m=ans[-1]
        #             if len(m)>len(i):
        #                 ans.append(i)
        # if len(ans)>=1:
        #     return ans[-1]
        
            



        

