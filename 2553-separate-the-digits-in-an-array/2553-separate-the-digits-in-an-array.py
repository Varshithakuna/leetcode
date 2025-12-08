class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        k=""
        for i in nums:
            i = str(i)
            k=k+i
        print(k)
        ans=[]
        for i in k:
            i=int(i)
            ans.append(i)
        return ans