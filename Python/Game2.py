

 nei = [(0,1),(0,-1),(1,0),(-1,0),(1,1),(1,-1),(-1,1),(-1,-1)]
 for i in range(r):
            for j in range(c):
                temp[i][j] = sum([board[i+ii][j+jj] if 0 <= i+ii < r and 0 <= j+jj < c else 0 for ii,jj in nei])
				
				
	"""			
				"""
class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m = len(board)
        n = len(board[0])
        #print (m, n) 
        board1 = [0]*m
        for i in range(m):
            board1[i] = [0]*n
            
        for i in range(m):
            print("I:", i)
            for j in range(n):              
                #print(board[i][j])
                state = board[i][j]
                neibs = 0
                #1-2
                if i-1 >= 0 and j-1 >= 0: neibs += board[i-1][j-1]; print(i,j,"^\ ",board[i][j] ,"_ ", board[i-1][j-1], neibs)
                if i-1 >= 0 : neibs += board[i-1][j]; print(i,j,"^| ",board[i][j] ,"_ ", board[i-1][j], neibs) 
                
                #3-4
                if i-1 >= 0 and j+1 < n: neibs += board[i-1][j+1]; print(i,j,"/^ ",board[i][j] ,"_ ", board[i-1][j+1]) 
                if j+1 < n : neibs += board[i][j+1]; print(i,j,"-> ",board[i][j] ,"_ ", board[i][j+1], "*") 
                
                #5-6
                if i+1 < m and j+1 < n: neibs += board[i+1][j+1]; print(i,j,"\. ",board[i][j] ,"_ ", board[i+1][j+1]) 
                if i+1 < m : neibs += board[i+1][j]; print(i,j,"|. ",board[i][j] ,"_ ", board[i+1][j]) 
                
                #7-8
                if i+1 <m and j-1 >= 0: neibs += board[i+1][j-1]; print(i,j,"./ ",board[i][j] ,"_ ", board[i+1][j-1]) 
                if j-1 >= 0 : neibs += board[i][j-1]; print(i,j,"<- ",board[i][j] ,"_ ", board[i][j-1], neibs) 
                
                if state == 1 and neibs < 2 : board1[i][j] = 0
                if state == 1 and (neibs == 3 or neibs == 2): board1[i][j] = 1
                if state == 1 and neibs > 3: board1[i][j] = 0
                if state == 0 and neibs == 3: board1[i][j] = 1
                
#        print(board1) 
        for i in range(m):
            for j in range(n):              
                board[i][j] = board1[i][j]        