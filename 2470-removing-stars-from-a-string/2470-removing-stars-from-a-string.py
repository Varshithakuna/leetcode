class Solution:
    def removeStars(self, s: str) -> str:
        p=[]
        for i in s:
            if i!='*':
                p.append(i)
            else:
                p.pop()
        return ''.join(p)


        