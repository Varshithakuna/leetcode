class Solution:
    def minimumChairs(self, s: str) -> int:
        c=[]
        v=[]
        for i in range(len(s)):
            if s[i]=="E":
                c.append(s[i])
                if len(v)>=1:
                    v.pop()
            elif s[i]=='L':
                v.append(s[i])
                if len(c)>=1:
                    c.pop()
        print(c)
        return len(c)+len(v)


        