class Solution:
    def isCircularSentence(self, s: str) -> bool:
        s=s.split(" ")
        ans=[]
        p=[]
        print(s)
        print(len(s))
        if len(s)==1:
            for i in s:
                if i[0]==i[len(i)-1]:
                    return True
                else:
                    return False
        for i in s:
            k=len(i)
            m=i[len(i)-1]
            ans.append(m)
            p.append(i[0])
        print(ans)
        print(p)
        c=0
        for i in range(len(ans)-1):
            if ans[i]==p[i+1]:
                c=c+1
        if c==len(ans)-1 and ans[-1]==p[0]:
            return True
        else:
            return False


        