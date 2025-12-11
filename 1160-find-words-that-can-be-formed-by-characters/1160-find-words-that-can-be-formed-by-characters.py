class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        ans=0
        for i in words:
            f=0
            for j in range(len(i)):
                if i.count(i[j])<=chars.count(i[j]):
                    continue
                else:
                    f=1
                    break
            if f==0:
                ans=ans+len(i)
        return ans

        