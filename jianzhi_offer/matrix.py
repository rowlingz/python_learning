# 输入一个矩阵，按照从外向里以顺时针的顺序依次打印出每一个数字，
# 例如，如果输入如下矩阵： 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16
# 则依次打印出数字1,2,3,4,8,12,16,15,14,13,9,5,6,7,11,10.

class Solution:
    # matrix类型为二维列表，需要返回列表
    def printMatrix(self, matrix):
        n = len(matrix)
        m = len(matrix[0])
        s = []
        left, right = 0, m - 1
        top, bottom = 0, n - 1
        i = top
        while left <= right and top <= bottom:
            for j in range(left, right + 1):
                s.append(matrix[i][j])
            for i in range(top + 1, bottom + 1):
                s.append(matrix[i][j])
            if bottom != top:
                for j in range(right-1, left-1, -1):
                    s.append(matrix[i][j])
            if left != right:
                for i in range(bottom - 1, top, -1):
                    s.append(matrix[i][j])
            left += 1
            right -= 1
            top += 1
            bottom -= 1
        return s


s = Solution()
matrix = [[1],[2],[3]]
matrix1 = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
matrix2 = [[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15]]
matrix3 = [[1,2,3]]
print(s.printMatrix(matrix))
print(s.printMatrix(matrix1))
print(s.printMatrix(matrix2))
print(s.printMatrix(matrix3))