class Solution:
    def isPalindrome(self, s: str) -> bool:
        c=""
        for i in s:
            if i.isupper():
                c=c+i.lower()
            elif i.islower():
                c=c+i
            elif i.isnumeric():
                c=c+i
        if c[::-1]==c:
            return True
        else:
            return False
