class Solution:
    def minOperations(self, nums: List[int], k1: int) -> int:
        d=set(nums)
        d=list(d)
        if len(d)==1 and d[0]==k1:
            return 0
        elif len(d)==1 and d[0]>k1:
            return 1
        elif len(d)==1 and d[0]<k1:
            return -1
        s=[]
        c=0
        for j in range(len(nums)):
            c=c+1
            for i in range(len(nums)):
                m=set(nums)
                m=list(m)
                m=sorted(m)
                if len(m)>=2:
                    h=m[-2]
                else:
                    h=m[-1]
                if nums[i]>h:
                    nums[i]=h
            k=set(nums)
            if len(k)==1:
                k=list(k)
                s.append(k)
                break
        print(s)
        v=s[0]
        w=v[0]
        if w<k1:
            return -1
        elif w==k1:
            return c
        else:
            return c+1