class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        s=nums.copy()
        for i in s:
            i=str(i)
            i=i[::-1]
            i=int(i)
            nums.append(i)
        print(nums)
        nums=set(nums)
        return len(nums)
        