class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        p=[0]
        for i in range(len(gain)):
            p.append(sum(gain[:i+1:]))
        return max(p)
        