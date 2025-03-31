class Solution:
    def reverseWords(self, s: str) -> str:
        s=s.strip()
        s=s.split()
        m=s[::-1]
        print(m)
        p=""
        return " ".join(m)
        

        