class Solution:
    def splitWordsBySeparator(self, words: List[str], separator: str) -> List[str]:
        w=[]
        for i in words:
            for j in i.split(separator): 
                if j:
                    w.append(j)
        return w
        