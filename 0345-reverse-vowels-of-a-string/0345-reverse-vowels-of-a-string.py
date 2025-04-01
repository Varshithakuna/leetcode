class Solution:
    def reverseVowels(self, s: str) -> str:
        ans=[]
        v=["A","a","e","E","i","I","O","o","U","u"]
        for i in s:
            if i in v:
                ans.append(i)
        ans = ans[::-1]
        h=[]
        for i in s:
            h.append(i)
        k=[]
        m=0
        for i in range(len(h)):
            if h[i] in v:
                k.append(ans[m])
                m=m+1
            else:
                k.append(h[i])
        return ''.join(k)


        
            
        