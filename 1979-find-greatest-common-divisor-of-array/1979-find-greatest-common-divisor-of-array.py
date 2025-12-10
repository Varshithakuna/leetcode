class Solution:
    def findGCD(self, nums: List[int]) -> int:
        n=max(nums)
        m=min(nums)
        r=math.gcd(n,m)
        print(r)
        return r

        