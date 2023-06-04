class Solution:
    def setZeroes(self, matrix):
        self.matrix = matrix
        self.m=len(self.matrix)
        self.n = len(self.matrix[0])

        zeroes = self.findZero()
        for r,c in list(zeroes):
            self.setColumn(c)
            self.setRow(r)
        return self.matrix

    def setRow(self, rowNo):
        self.matrix[rowNo] = [0]*self.n
    
    def setColumn(self,columnNo):
        for i in range(self.m):
            self.matrix[i][columnNo]=0
        

    def findZero(self):
        for i in range(self.m):
            for j in range(self.n):
                if self.matrix[i][j]==0:
                    yield (i, j)
        

