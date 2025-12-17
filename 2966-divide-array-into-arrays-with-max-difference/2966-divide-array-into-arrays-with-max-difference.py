class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        ans=[]
        nums=sorted(nums)
        for i in range(0,len(nums),3):
            ans.append([nums[i],nums[i+1],nums[i+2]])
        print(ans)
        for i in ans:
            c=0
            for j in range(len(i)-1):
                c=c+abs(i[j]-i[j+1])
                if c<=k:
                    continue
                else:
                    return []
        return ans

        