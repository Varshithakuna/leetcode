class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        flag=0
        for i in nums:
            if nums.count(i)%2!=0:
                flag=1
                break
        if flag==0:
            return True
        else:
            return False
        