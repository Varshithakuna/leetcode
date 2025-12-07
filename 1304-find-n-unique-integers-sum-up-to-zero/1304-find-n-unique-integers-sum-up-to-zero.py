class Solution:
    def sumZero(self, n: int) -> List[int]:
        ans=[]
        for i in range((n//2)+1):
            ans.append(i)
        print(ans)
        for i in range(1,len(ans)):
            if sum(ans)!=0:
                ans.append(-i)
            else:
                break
        print(ans)
        if len(ans)==n:
            return ans
        else:
            ans.remove(0)
            return ans
            

        