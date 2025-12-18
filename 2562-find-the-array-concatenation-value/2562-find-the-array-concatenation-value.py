class Solution:
    def findTheArrayConcVal(self, nums: List[int]) -> int:
        c=0
        while len(nums)>=2:
            t=nums.pop(0)
            b=nums.pop()
            n=str(t)+str(b)
            print(n)
            c=c+int(n)
        for i in nums:
            c=c+i
        return c
        