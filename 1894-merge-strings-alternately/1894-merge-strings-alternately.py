class Solution:
    def mergeAlternately(self, w1: str, w2: str) -> str:
        if len(w1)>len(w2):
            ans=""
            for i in range(len(w1)):
                ans=ans+w1[i]
                if len(w2)-1>=i:
                    ans=ans+w2[i]
            return ans
        elif len(w2)>len(w1):
            ans=""
            for i in range(len(w2)):
                if len(w1)-1>=i:
                    ans=ans+w1[i]
                ans=ans+w2[i]
            return ans
        else:
            ans=""
            for i,j in zip(w1,w2):
                ans=ans+i
                ans=ans+j
            return ans
