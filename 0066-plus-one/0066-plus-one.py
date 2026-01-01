class Solution:
    def plusOne(self, a: List[int]) -> List[int]:
        k=[]
        k1=[]
        v=[]
        s=" "
        for i in range(len(a)):
            a[i]=str(a[i])
            k.append(a[i])
        for i in range(len(k)):
            s=s+k[i]
        s=int(s)+1
        s=list(str(s))
        for i in range(len(s)):
            s[i]=int(s[i])
            v.append(s[i])
        return v
      
        