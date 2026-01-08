class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        arr=[]
        n=str(num)
        for i in range(len(n)):
            arr.append(n[i:i+k])
        print(arr)
        ans=0
        for i in arr:
            m=i
            i = int(i)
            if i!=0 and num%i==0 and len(m)==k:
                ans=ans+1
        return ans

        