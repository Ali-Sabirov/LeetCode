class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:

        #print(matrix)
        n = len(matrix[0])
        m1 = [0]*n
        for i in range(n):
            m1[i] = [0]*n
        for i in range(n):
            for j in range(n):
                k = n-i-1
                m1[j][k] = matrix[i][j]
        #print(m1)   
        for i in range(n):
            for j in range(n):             
                matrix[i][j] = m1[i][j]  