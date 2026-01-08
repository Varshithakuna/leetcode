class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        # d={}
        # for i in nums:
        #     if i not in d:
        #         d[i]=1
        #     else:
        #         d[i]=d[i]+1

        # k = []
        # for i in d:
        #     k.append(i)
        fin =[]
        n = len(nums)
        nums=set(nums)
        for i in range(1,n+1):
            if i not in nums:
                fin.append(i)
        return fin

        