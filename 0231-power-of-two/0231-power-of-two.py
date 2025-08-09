class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if (n==1 or n==2):
            return True
        elif (n%2==0 ):
            k=1
            for i in range(31):
                k=(2**i*k)
                if (k==n):
                    return True
                else:
                    k=1
            else:
                return False
        else:
            return False
     
                
            
                


        