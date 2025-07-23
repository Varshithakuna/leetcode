class Solution:
    def buddyStrings(self, s: str, g: str) -> bool:
        c=0
        # k1=list(s)
        # l=set(k1)
        # k2=list(g)
        # l1=set(k2)
        # if k1==k2 and len(k1)==len(l) and len(k2)==len(l1):
        #     return False 
        s=list(s)
        k=set(s)
        g=list(g)
        m=set(g)
        ans=[]
        f=[]
        h=[]
        if len(s)!=len(g) or len(s)==1:
            return False
        if s==g:
            if len(m)==1:
                return True
            elif s==g and len(s)==len(m):
                return False
        for i in range(len(s)):
            ans.append([s[i],i])
        ans2=[]
        for i in range(len(g)):
            ans2.append([g[i],i])
        for i,j in zip(ans,ans2):
            if i[0]!=j[0]:
                f.append([i[0],j[0]])
        print(f)
        if len(f)==0:
            return True
        elif len(f)==2 and  f[0][::-1]==f[1]:
            return True
        else:
            return False


                    

        