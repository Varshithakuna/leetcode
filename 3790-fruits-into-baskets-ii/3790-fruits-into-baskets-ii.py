class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        d=[]
        a=0
        for i in fruits:
            for j in range(len(baskets)):
                if i<=baskets[j]:
                    baskets.pop(j)
                    break
            else:
                a=a+1
        return a



