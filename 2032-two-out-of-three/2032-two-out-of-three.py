class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        ans=set()
        for i in nums1:
            if i in nums3 or i in nums2:
                ans.add(i)
        for i in nums2:
            if i in nums3 or i in nums1:
                ans.add(i)
        ans=list(ans)
        return ans
        