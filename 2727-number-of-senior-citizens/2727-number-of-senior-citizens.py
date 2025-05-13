class Solution:
    def countSeniors(self, d: List[str]) -> int:
        ans=[]
        for i in d:
            k=""
            k=k+i[11]
            k=k+i[12]
            m=int(k)
            if m>60:
                ans.append(m)
        return len(ans)
        
        