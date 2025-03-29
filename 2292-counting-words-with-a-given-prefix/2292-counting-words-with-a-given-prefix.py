class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        s=[]
        for i in words:
            if pref in i:
                s.append(i)
        c=0
        for i in s:
            for j in range(len(i)):
                    m=i[:j+1:]
                    m=''.join(m)
                    if m==pref:
                        c=c+1
                        break
        return c



            
        