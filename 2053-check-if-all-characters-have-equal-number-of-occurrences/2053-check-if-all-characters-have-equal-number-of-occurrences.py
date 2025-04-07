class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        d=set()
        k=[]
        for i in s:
            d.add(s.count(i))
            if s.count(i) in d:
                k.append(i)
            else:
                return False
                break
        if len(d)==1:
            return True
        else:
            return False

        