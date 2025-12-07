class Solution:
    def earliestTime(self, tasks: List[List[int]]) -> int:
        k=[]
        for i in tasks:
            k.append(sum(i))
        return min(k)
        