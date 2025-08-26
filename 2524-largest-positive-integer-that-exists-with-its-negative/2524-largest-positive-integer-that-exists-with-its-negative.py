class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        k=[]
        for i in nums:
            if i<0 and abs(i) in nums:
                k.append(abs(i))
        if len(k)>0:
            return max(k)
        else:
            return -1
        