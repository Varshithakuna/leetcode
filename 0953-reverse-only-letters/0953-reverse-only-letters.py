class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        # p=""
        # v=s.split("-")
        # v=v[::-1]
        # o=[]
        # for i in v:
        #     i=i[::-1]
        #     o.append(i)
        # o="".join(o)
        # m=[]
        # p=[]
        # for i in range(len(o)):
        #     if o[i].isalpha():
        #         m.append(o[i])
        #     else:
        #         p.append(i)
        # for i in p:
        #     m.insert(i,s[i])
        # return ''.join(m)
        p=[]
        q=[]
        for i in range(len(s)):
            if s[i].isalpha():
                p.append(s[i])
            else:
                q.append(i)
        p=p[::-1]
        for i in q:
            p.insert(i,s[i])
        return ''.join(p)


        
                
        

        

        