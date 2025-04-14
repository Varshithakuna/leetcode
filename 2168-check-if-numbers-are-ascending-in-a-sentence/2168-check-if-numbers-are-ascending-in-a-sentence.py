class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        s=s.split(" ")
        print(s)
        a="1234567890"
        p=[]
        for i in s:
            c=0
            for j in i:
                if j in a:
                    c=c+1
            if c>0:
                i=int(i)
                p.append(i)
        m=set(p)
        if p==sorted(p) and len(p)==len(m):
            return True
        else:
            return False
        


        