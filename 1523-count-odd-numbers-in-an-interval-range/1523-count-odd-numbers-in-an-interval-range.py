class Solution:
    def countOdds(self, low: int, high: int) -> int:
        if ((low+high)%2==0):
            s=(low+high)//2
            if (low%2==0):
                s=s-low
                return s
            else:
                s=s-low
                return s+1
        else:
            s1=((low+high)//2)+1
            s1=s1-low
            return s1

        