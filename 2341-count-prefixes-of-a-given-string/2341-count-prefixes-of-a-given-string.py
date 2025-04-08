class Solution:
    def countPrefixes(self, words: List[str], s: str) -> int:
        p=[]
        for i in range(len(s)):
            p.append(s[:i+1])
        c=0
        for i in words:
            if i in p:
                c=c+1
        return c

        