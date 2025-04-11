class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        ans=[]
        for i in arr:
            if arr.count(i)==1:
                ans.append(i)
        k1=k-1
        if len(ans)>=k:
            return (ans[k1])
        return ""
        