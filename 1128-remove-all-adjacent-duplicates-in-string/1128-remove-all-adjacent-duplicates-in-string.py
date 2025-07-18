class Solution:
    def removeDuplicates(self, s: str) -> str:
        ans=[]
        right = len(s)
        for i in range(len(s)):
            if len(ans)==0:
                ans.append(s[i])
            elif s[i]!= ans[-1]:
                ans.append(s[i])
            else:
                ans.pop()
        print(ans)
        return ''.join(ans)
            

        