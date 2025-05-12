class Solution:
    def vowelStrings(self, words: List[str], left: int, right: int) -> int:
        c=0
        k="aeiou"
        ans=[]
        for i in range(left,right+1):
            ans.append(words[i])
        for i in ans:
            m=len(i)
            if i[0] in k and i[m-1] in k  :
                c=c+1
                
        return c
        

                