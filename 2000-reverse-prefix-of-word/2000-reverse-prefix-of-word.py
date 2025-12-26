class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        if ch not in word:
            return word
        else:
            m=word.index(ch)
            s=word[:m+1:]
            k=word[m+1::]
            s=s[::-1]
            h=s+k
            return h
            
        