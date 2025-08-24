class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        m=sum(nums)
        c=0
        n=0
        for i in nums:
            v=str(i)
            for j in range(len(v)):
                c=c+int(v[j])
        print(c)
        return abs(m-c)

        