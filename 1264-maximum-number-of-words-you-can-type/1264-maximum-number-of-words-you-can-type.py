class Solution:
    def canBeTypedWords(self, text: str, b: str) -> int:
        text = text.split(" ")
        m=0
        for i in text:
            c=0
            for j in range(len(i)):
                if i[j] not in b:
                    c=c+1
                else:
                    break
            if c== len(i):
                m=m+1
        return m

            
            
        
        