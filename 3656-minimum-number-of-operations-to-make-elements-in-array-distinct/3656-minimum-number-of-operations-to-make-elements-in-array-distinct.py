class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        n1=sorted(nums)
        n=set(nums)
        n=list(n)
        n=sorted(n)
        if n1==n:
            return 0
        c=0
        s=set()
        for i in range(0,len(nums),3):
            c=c+1
            num=nums[i+3:len(nums)]
            num=sorted(num)
            k=set(num)
            k=list(k)
            k=sorted(k)
            if k==num:
                break
        return c


        