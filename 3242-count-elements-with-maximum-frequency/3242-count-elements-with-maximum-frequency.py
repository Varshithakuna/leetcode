class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        ans=[]
        s=set(nums)
        s=list(s)
        for i in s:
            ans.append(nums.count(i))
        a=max(ans)
        print(ans)
        print(a)
        m=[]
        for i in ans:
            if a==i:
                m.append(i)
        return sum(m)
        