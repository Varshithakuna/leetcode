class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        for i in words:
            m=i
            m=m[::-1]
            if m==i:
                return i
        else:
            return ""
        