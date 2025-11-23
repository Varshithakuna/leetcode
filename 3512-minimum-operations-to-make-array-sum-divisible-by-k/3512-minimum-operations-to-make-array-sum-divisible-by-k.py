class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        c=0
        m=sum(nums)
        n=m
        if n%k==0:
            return c
        else:
            for i in range(m):
                n=n-1
                c=c+1
                if n%k==0:
                    return c
                    break


        