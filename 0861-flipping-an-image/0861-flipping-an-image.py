class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        ans=[]
        for i in image:
            i=i[::-1]
            ans.append(i)
        for i in ans:
            for j in range(len(i)):
                if i[j]==0:
                    i[j]=1
                else:
                    i[j]=0
        return ans
        