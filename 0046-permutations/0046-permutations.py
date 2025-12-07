from itertools import permutations
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = list(permutations(nums))
        ans=[]
        for i in res:
            i =  list(i)
            ans.append(i)
        print(ans)
        return ans


        