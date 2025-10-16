class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        nums.sort()
        res=sorted(nums,key=lambda x:(nums.count(x),-x))
        return res
       
    





        