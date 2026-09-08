class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.mat = matrix
        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        ans = 0
        i=row1
        while i <= row2:
            for j in range(col1,col2+1):
                ans += self.mat[i][j]
            i+=1
        return ans

        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)