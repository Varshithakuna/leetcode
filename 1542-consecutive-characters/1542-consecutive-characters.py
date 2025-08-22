class Solution:
    def maxPower(self, s: str) -> int:
        ans=[]
        for i in range(len(s)):
            c=0
            for j in range(i+1,len(s)):
                if s[i]==s[j]:
                    c=c+1
                else:
                    break
            ans.append(c)
        return max(ans)+1
            

        