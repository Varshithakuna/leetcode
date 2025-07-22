class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        ans=['0']*len(s)
        for i in range(len(s)):
            k=indices[i]
            ans[k]=s[i]
        print(ans)
        return ''.join(ans)

        