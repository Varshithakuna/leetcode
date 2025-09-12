class Solution:
    def doesAliceWin(self, s: str) -> bool:
        a="AEIOUaeiou"
        ans=[]
        for i in s:
            if i in a:
                ans.append(i)
        if len(ans)>0:
            return True
        else:
            return False

        