class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        res=[]
        d={}
        for i in range(0,10):
            if str(i) not in d:
                d[str(i)]=0
        for i in digits:
            if str(i)  in d:
                d[str(i)]+=1
        print(d)
        for i in range(100,1000,2):
            m=str(i)
            flag=0
            for j in range(len(m)):
                if d[m[j]]<(m.count(m[j])):
                    flag=1
                    break
            if flag==0:
                res.append(int(m))
        print(res)
        return res
                    



        
            
        