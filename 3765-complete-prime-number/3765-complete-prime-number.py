class Solution:
    def completePrime(self, num: int) -> bool:
        ans=[]
        def prime(digit):
            if digit<2:
                return 0
            for i in range(2,int(sqrt(digit))+1):
                if digit%i==0:
                    return 0
            return 1
        n= str(num)
        for i in range(len(n)):
            s=n[:i+1]
            s=''.join(s)
            s=int(s)
            ans.append(s)
        for i in range(len(n)):
            k=n[i+1::]
            k=''.join(k)
            if len(k)>0  and int(k) not in ans:
                ans.append(int(k))
        m=[]
        for i in ans:
            if not prime(i):
                return False    
        return True

  



        