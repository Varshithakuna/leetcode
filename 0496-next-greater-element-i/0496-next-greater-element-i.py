class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans=[]
        for i in range(len(nums1)):
            s=nums2.index(nums1[i])
            a=nums2[s:]
            for j in range(len(a)):
                if nums1[i]<a[j]:
                    ans.append(a[j])
                    break
            else:
                ans.append(-1)
        return ans