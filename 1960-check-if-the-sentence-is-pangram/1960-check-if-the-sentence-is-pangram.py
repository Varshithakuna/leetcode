class Solution:
    def checkIfPangram(self, s: str) -> bool:
        s=list(s)
        print(s)
        s=set(s)
        if len(s)==26:
            return True
        else:
            return False

        