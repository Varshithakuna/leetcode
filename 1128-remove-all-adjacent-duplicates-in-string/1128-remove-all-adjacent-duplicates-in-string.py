class Solution:
    def removeDuplicates(self, s: str) -> str:
        ans=[s[0]]
        right = len(s)
        for i in range(1,len(s)):
            if len(ans)==0:
                ans.append(s[i])
            elif s[i]!= ans[-1]:
                ans.append(s[i])
            else:
                ans.pop()
        print(ans)
        return ''.join(ans)
            

        