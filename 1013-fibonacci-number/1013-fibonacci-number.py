class Solution:
    def fib(self, n: int) -> int:
        a,b=0,1
        if(n==0):
            return 0
        for i in range(n-1):
            c=a+b
            a,b=b,c
        return b
