class Solution:
    def groupThePeople(self, g: List[int]) -> List[List[int]]:
        d={}
        fin=[]
        for i in range(len(g)):
            if g[i] not in d:
                d[g[i]]=[i]
            else:
                d[g[i]].append(i)
        for i1 in d:
            m=d[i1]
            for j in range(0,len(m),i1):
                fin.append(m[j:i1+j])
        return fin
        

                
           