class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        s1="AEIOUaeiou"
        m=len(s)//2
        ans=s[:m]
        pans=s[m::]
        c=0
        d=0
        for i in ans:
            if i in s1:
                c=c+1
        for i in pans:
            if i in s1:
                d=d+1
        if d==c:
            return True
        else:
            return False

        