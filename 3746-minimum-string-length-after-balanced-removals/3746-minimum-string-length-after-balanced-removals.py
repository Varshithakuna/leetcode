class Solution:
    def minLengthAfterRemovals(self, s: str) -> int:
        c=s.count('a')
        k=s.count('b')
        return abs(c-k)

        