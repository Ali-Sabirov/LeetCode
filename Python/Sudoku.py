class Solution: 
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n = len(board)
        m = int(sqrt(n))
        ret = 1
        for i in range(n):
            ret *= check_row(board[i])
        a = []
        for i in range(n):
            for j in range(n):
                a.append(board[j][i])
            ret *= check_row(a)
            a.clear()
            
        for i in range(0,n,m):
            for j in range(0,n,m):
                print('SQR')
                for k in range(0,m):
                    for l in range(0,m):
                        print('[', i+k,',', j+l,']', end=' ' )
                        a.append(board[i+k][j+l])
                print()    
                ret *= check_row(a)
                a.clear()    
        return ret
def check_row(b: List):
    a = []
    n = len(b)
    j = 0
    for i in range(n):
        if b[i] == '.':
            True
        else:    
            a.append(int(b[i]))
            j += 1
    if j == 0: return True      
    if(min(a) < 1 and max(a) > n):
        print("Значение вне интервала [1,9] ",min(a), max(a) )
        return False
    set_a = set(a)
    if len(set_a) < len(a):
        print("Дубль", end=' ' )
        print('[', end = ' ')
        for i in range(n):
            print(b[i], sep=',', end=' ')
        print(']')
        return False   
    return True