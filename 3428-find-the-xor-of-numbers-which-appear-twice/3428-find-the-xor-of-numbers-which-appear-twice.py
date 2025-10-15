class Solution:
    def duplicateNumbersXOR(self, nums: List[int]) -> int:
        s=set(nums)
        s=list(s)
        q=[]
        for i in s:
            if nums.count(i)==2:
                q.append(i)
        c=0
        for i in q:
            c=c^i
        return c



        