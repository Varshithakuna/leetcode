class Solution:
    def findThePrefixCommonArray(self, a: List[int], b: List[int]) -> List[int]:
        ans=[]
        def f(s,v):
            c=0
            for i in s:
                if i in v:
                    c=c+1
            ans.append(c)
        for i in range(len(a)):
            s=a[:i+1]
            v=b[:i+1]
            f(s,v)
        print(ans)
        return ans
            

        