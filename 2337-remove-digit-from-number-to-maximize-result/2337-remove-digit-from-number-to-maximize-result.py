class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        s1=[]
        for i in range(len(number)):
            if number[i]==digit:
                k=number[:i]
                m=number[i+1:]
                s=k+m
                s=int(s)
                s1.append(s)
        l=max(s1)
        return str(l)

        