class Solution:
    def findIntersectionValues(self, nums1: List[int], nums2: List[int]) -> List[int]:
        k=nums1.copy()
        v=nums2.copy()
        ans=0
        s=0
        for i in nums1:
            if i in nums2:
                s=s+1
        for i in nums2:
            if i in nums1:
                ans=ans+1

        return [s,ans]

        