class Solution:
    def capitalizeTitle(self, title: str) -> str:
        t = title.split(" ")
        p=[]
        for i in t:
            if len(i)<=2:
                q=i.lower()
                print(q)
                p.append(q +" ")
            if len(i)>2:
                m=i[0].upper()
                s=i[1:len(i)]
                s=s.lower()
                s=m+s
                p.append(s+" ")     
        x= ''.join(p)
        x=x.strip()
        return x
        