class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        c=0
        w1 =[]
        for i in words1:
            if words1.count(i)==1:
                w1.append(i)
        w2=[]
        for i in words2:
            if words2.count(i)==1:
                w2.append(i)
        for i in w1:
            if i in w2:
                c=c+1
        return c