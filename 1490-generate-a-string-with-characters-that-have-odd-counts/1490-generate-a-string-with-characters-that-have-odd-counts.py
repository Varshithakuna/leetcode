class Solution:
    def generateTheString(self, n: int) -> str:
        a=[]
        for i in range(n-1):
            a.append('a')
        if n%2==0:
            a.append('b')
        else:
            a.append('a')
        return ''.join(a)
        