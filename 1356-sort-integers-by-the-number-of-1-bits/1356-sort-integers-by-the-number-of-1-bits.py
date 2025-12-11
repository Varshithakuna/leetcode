class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        arr=sorted(arr)
        ans=[]
        for i in arr:
            s=bin(i)[2:]
            ans.append(s)
        print(ans)
        d=[]
        for i in ans:
            d.append([int(str(i),2),i.count('1')])
        print(d)
        d.sort(key=lambda x: x[1])
        print(d)
        res=[]
        for i in d:
            res.append(i[0])
        return res

        