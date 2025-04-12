class Solution:
    def checkString(self, s: str) -> bool:
        if s.count('a')==0:
            return True
        c=0
        for i in s:
            if i!='b':
                c=c+1
            else:
                break
        print(c)
        m=s[:c+1]
        k=s[c+1:len(s)]
        print(k)
        if 'a' in k:
            return False
        else:
            return True