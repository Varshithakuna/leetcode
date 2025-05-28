class Solution:
    def minimizedStringLength(self, s: str) -> int:
        k=[]
        for i in s:
            k.append(i)
        k=set(k)
        return len(k)
        