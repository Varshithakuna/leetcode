class Solution:
    def strStr(self, h: str, n: str) -> int:
        ans=[]
        for i in range(len(h)):
            if n in h[:i+1:]:
                return h.index(n)
        else:
            return -1
        