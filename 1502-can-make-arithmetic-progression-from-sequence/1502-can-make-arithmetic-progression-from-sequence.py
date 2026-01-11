class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr=sorted(arr)
        ans=[]
        for i in range(1,len(arr)):
            if len(ans)==0:
                ans.append(abs(arr[i-1]-arr[i]))
            elif (abs(arr[i-1]-arr[i])) in ans:
                continue
            else:
                return False
        return True

        