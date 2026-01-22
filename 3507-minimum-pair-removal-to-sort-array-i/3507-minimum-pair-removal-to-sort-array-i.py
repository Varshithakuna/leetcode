class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        if sorted(nums)==nums:
            return 0
        k = sorted(nums)
        c=0
        for l in range(len(nums)):
            n=[]
            m=[]
            for j in range(len(nums)-1):
                n.append(nums[j]+nums[j+1])
                m.append([j,j+1])
            h=min(n)
            h=n.index(h)
            m=m[h]
            print(m)
            s=[]
            for i in range(len(nums)):
                if i!=m[0] and i!=m[1]:
                    s.append(nums[i])
            s.insert(m[0],min(n))
            print(s)
            nums = s
            c=c+1
            if sorted(nums)==nums:
                return c
            else:
                continue
            
