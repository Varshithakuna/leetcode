class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        m=strs
        s=[]
        for i in range(len(strs)):
            k=''.join(sorted(strs[i]))
            s.append(k)
        l=[]
        ans=[]
        for i in range(len(s)):
            if s[i] not  in l:
                n=[m[i]]
                l.append(s[i])
                for j in range(i+1,len(s)):
                    if s[i]==s[j]:
                        n.append(m[j])
                ans.append(n)
        return ans


                    




        

        