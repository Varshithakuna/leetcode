class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        ans=[]
        for i in s:
            if i in t:
                ans.append(i)
        left =0
        right = len(t)
        h=0
        n=[]
        if t in s:
            return 0
        print(ans)
        c=0
        while left<=right and h<len(ans):
            if t[left]==ans[h]:
                left=left+1
                h=h+1
                c=c+1
            else:
                h=h+1
        print(c)
        return abs(len(t)-c)


        
            
                
        