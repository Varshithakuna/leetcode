# class Solution:
#     def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
#         # ans=[] 
#         # k=[]   
#         # for i in nums1:
#         #     if i not in nums2 and i not in k:
#         #         k.append(i)
#         # k1=[]
#         # for j in nums2:
#         #     if j not in nums1 and j not in k:
#         #         k1.append(j) 
#         # ans.append(k)
#         # ans.append(k1)
#         # return ans
class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        set1, set2 = set(nums1), set(nums2)
        return [list(set1 - set2), list(set2 - set1)]

                

        