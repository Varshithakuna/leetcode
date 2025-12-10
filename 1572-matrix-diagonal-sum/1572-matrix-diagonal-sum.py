class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        c=0
        h=0
        n=len(mat)
        for i in range(n):
            for j in range(len(mat[i])):
                if i==j:
                    c=c+mat[i][j]
                if i+j==(n-1) and i!=j:
                    c=c+mat[i][j]
        return c


        