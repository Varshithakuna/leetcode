class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        d=set()
        for i in s:
            d.add(s.count(i))
        if len(d)==1:
            return True
        else:
            return False

        