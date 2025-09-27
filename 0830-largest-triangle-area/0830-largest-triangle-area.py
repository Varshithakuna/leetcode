class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        res = 0
        for i in range(len(points) - 2):
            for j in range(i + 1, len(points) - 1):
                for k in range(j + 1, len(points)):
                    ax, ay = points[j][0] - points[i][0], points[j][1] - points[i][1]
                    bx, by = points[k][0] - points[i][0], points[k][1] - points[i][1]
                    area = 0.5 * abs(ax * by - ay * bx)
                    res = max(res, area)
        
        return res