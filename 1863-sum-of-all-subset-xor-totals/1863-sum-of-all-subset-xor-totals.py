class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        a=[]
        res = 0
        for i in range(1,len(nums)+1):
            for combo in combinations(nums,i):
                a.append(combo)
        for i in a:
            k=0
            for j in i:
                k=k^j
            res=res+k
        return res

        
                    
        


        