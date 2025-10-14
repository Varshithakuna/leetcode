class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        ans=[]
        n=[]
        q=[]
        h=[]
        for i in words:
            if ans:
                if sorted(ans[-1])==sorted(i):
                    continue
                else:
                    ans.append(i)
            else:
                ans.append(i)

        return ans







