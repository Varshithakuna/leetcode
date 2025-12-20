class Solution:
    def findKOr(self, nums: List[int], k: int) -> int:
        y=k
        res=[]
        k=[]
        for i in nums:
            r=bin(i)[2:]
            res.append(r)
            k.append(len(r))
        ans=[]
        n=max(k)
        for i in res:
            if len(i)==n:
                ans.append(i)
            else:
                i=list(i)
                for j in range(n-len(i)):
                    i.insert(0,'0')
                i=''.join(i)
                ans.append(i)
        print(ans)
        fans=[]
        for i in range(n):
            c=[]
            for j in ans:
                c.append(j[i])
            fans.append(c)
        g=[]
        for i in fans:
            print(i)
            if i.count('1')>=y:
                g.append('1')
            else:
                g.append('0')
        print(g)
        g=''.join(g)
        return int(g,2)

        