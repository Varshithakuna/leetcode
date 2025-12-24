class Solution:
    def minimumBoxes(self, apple: List[int], c: List[int]) -> int:
        n=sum(apple)
        c=sorted(c)[::-1]
        k=0
        o=0
        for i in c:
            if k<n:
                k=k+i
                o=o+1
        return o
        


        