class Solution:
    def percentageLetter(self, s: str, letter: str) -> int:
        m=s.count(letter)
        return int(m/len(s)*100)
        