class Solution:
    def rotate(self, mat: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        ans=[]
        for i in range(len(mat)):
            temp=[]
            for j in range(len(mat)-1,-1,-1):
                temp.append(mat[j][i])
            ans.append(temp)
        print(ans)
        for i in range(len(mat)):
            mat[i]=ans[i]
        return mat
        
        