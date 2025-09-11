class Solution:
    def sortVowels(self, s: str) -> str:
        ans=[]
        a="AEIOUaeiou"
        for i in s:
            if i  in a:
                ans.append(i)
        ans=sorted(ans)
        fin = []
        for i in range(len(s)):
            if s[i] in a:
                fin.append(ans[0])
                ans.pop(0)
            else:
                fin.append(s[i])
        print(fin)
        return ''.join(fin)


        