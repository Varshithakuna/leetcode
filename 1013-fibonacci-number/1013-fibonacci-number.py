class Solution:
    def fib(self, n: int) -> int:
        c=0
        a=0
        b=1
        if n<1:
            return 0
        for i in range(2,n+1):
            c=a+b
            a=b
            b=c
        return b


        

            

        