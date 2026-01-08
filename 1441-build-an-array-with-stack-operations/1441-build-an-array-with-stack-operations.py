class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        s=[]
        p=[]
        for i in range(1,n+1):
            if i in target:
                s.append("Push")
                p.append(i)
                if p==target:
                    break
            else:
                s.append("Push")
                s.append("Pop")
        return s
 
        

            

        