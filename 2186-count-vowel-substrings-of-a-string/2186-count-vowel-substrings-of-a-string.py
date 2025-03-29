class Solution:
    def countVowelSubstrings(self, word: str) -> int:
        ans=[]
        v="aeiou"
        c=[]
        for i in range(len(word)):
            for j in range(i,len(word)):
                ans.append(word[i:j+1])
        for i in ans:
            temp=""
            for j in i:
                    temp=temp+j
            s =list(temp)
            s=set(s)
            s=sorted(s)
            s=''.join(s)
            if s=="aeiou":
                c.append(i)
        return len(c)

        



        