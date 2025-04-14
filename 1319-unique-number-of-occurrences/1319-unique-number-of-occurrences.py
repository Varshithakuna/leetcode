class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        w = set(arr)
        w = list(w)
        count =0
        v=[]
        for i in range(len(w)):
            v.append(arr.count(w[i]))
        x = set(v)
        x = list(x)
        if (len(v)==len(x)):
            return True
        else :
            return False




        