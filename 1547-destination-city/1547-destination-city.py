class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        z=[]
        for i in paths:
            for j in range(len(i)):
                z.append(i[j])

        d=[]
        for i in paths:
            for j in range(len(i)):
                if z.count(i[1])==1:
                    d.append(i[j])
        print(d)
        return d[-1]


        