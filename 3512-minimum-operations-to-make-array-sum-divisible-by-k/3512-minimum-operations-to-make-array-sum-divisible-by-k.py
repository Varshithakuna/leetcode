class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        c=0
        m=sum(nums)
        n=m
        for i in range(m+1):
            if n%k==0:
                return c
                break
            else:
                c=c+1
                n=n-1


    