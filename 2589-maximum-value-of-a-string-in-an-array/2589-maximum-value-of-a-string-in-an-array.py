class Solution:
    def maximumValue(self, strs: List[str]) -> int:
        ans=[]
        for i in strs:
            if i.isnumeric():
                i=int(i)
                ans.append(i)
            else:
                ans.append(len(i))
        return max(ans)

        