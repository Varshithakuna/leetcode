class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        ans=[[] for i in range(len(nums))]
        for i in nums:
            j=0
            while i in ans[j]:
                j=j+1
            ans[j].append(i)        
        m=[]
        for i in ans:
            if i:
                m.append(i)
        print(m)
        return m
        

        