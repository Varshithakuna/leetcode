class Solution:
    def makeSmallestPalindrome(self, s: str) -> str:
        s=list(s)
        print(s)
        left = 0
        right = len(s)-1

        while left<right:
            if s[left]==s[right]:
                left = left+1
                right = right-1
                print(left)
                print(right)
            else:
                if ord(s[left])>=ord(s[right]):
                    s[left]=s[right]
                else:
                    s[right]=s[left]
        print(s)
        return "".join(s)


        