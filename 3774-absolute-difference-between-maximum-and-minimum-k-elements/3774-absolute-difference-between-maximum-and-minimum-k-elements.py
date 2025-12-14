class Solution:
    def absDifference(self, nums: List[int], k: int) -> int:
        nums=sorted(nums)
        s=[]
        n=nums[::-1]
        h=[]
        for i in range(k):
            s.append(nums[i])
        for i in range(k):
            h.append(n[i])
        print(s)
        print(h)
        if len(nums)==k:
            return 0
        return abs(sum(s)-sum(h))


        