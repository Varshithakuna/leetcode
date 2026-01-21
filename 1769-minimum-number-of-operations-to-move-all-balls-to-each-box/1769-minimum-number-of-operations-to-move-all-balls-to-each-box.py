class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        ans=[]
        for i in range(len(boxes)):
            c=0
            for j in range(len(boxes)):
                if i!=j and boxes[j]=="1":
                    c=c+abs(j-i)
            ans.append(c)
        return ans

        