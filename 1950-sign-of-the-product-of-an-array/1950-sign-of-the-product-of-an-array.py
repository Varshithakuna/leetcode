class Solution:
    def arraySign(self, nums: List[int]) -> int:
        p=1
        if 0 in nums:
            return 0
        for i in nums:
            p=p*i
        if p>0:
            return 1
        elif p<0:
            return -1
     
        