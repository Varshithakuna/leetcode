class Solution:
    def canAliceWin(self, nums: List[int]) -> bool:
        s=[]
        d=[]
        for i in nums:
            if i<=9:
                s.append(i)
            else:
                d.append(i)
        if sum(s)>sum(d):
            return True
        elif sum(d)>sum(s):
            return True
        else:
            return False
        