class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        ans=[]
        fin=[0]*len(ans)
        for i in range(len(s)):
            if s[i]==c:
                ans.append(i)
        for i in range(len(s)):
            k=[]
            k2=[]
            for j in ans:
                if i<j and i not in ans:
                    k.append(j)
                elif i not in ans and i>j:
                    k2.append(j)
            if len(k2)==0 and len(k)>0:
                u=abs(i-k[0])
                fin.insert(i,u)
            elif len(k)==0 and len(k2)>0:
                h=abs(i-k2[-1])
                fin.insert(i,h)
            elif len(k)>0 and len(k2)>0:
                m=min(abs(i-k[0]),abs(i-k2[-1]))
                fin.insert(i,m)
                print(m)
            else:
                fin.insert(i,0)
            print(k)
            print(k2)
        return fin


    