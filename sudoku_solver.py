# Sovler class uswing backtracking algorithm

class SudokuSolver:
    
    @staticmethod
    def is_valid(board,row,col,num):
        
        # Check row
        for x in range(9):
            if board[row][x] == num:
                return False
            
        # check col
        for x in range(9):
            if board[x][col] == num:
                return False
            
        # check 3X3 box
        start_row, start_col = 3 * (row // 3), 3 * (col //3)
        for i in range(3):
            for j in range(3):
                if board[i + start_row][j + start_col] == num:
                    return False
        
        return True
    
    # find Empty cell
    @staticmethod
    def find_empty(board):
        
        for i in range(9):
            for j in range(9):
                if board[i][j] == 0:
                    return(i,j)
                
        return None
    
    # Solve board
    @staticmethod
    def solve(board):
        
        empty = SudokuSolver.find_empty(board)
        
        if not empty:
            return True # No empty cell, puzzle is solved
        
        row, col = empty
        
        for num in range(1, 10):
            if SudokuSolver.is_valid(board, row, col, num):
                board[row][col] = num
                
                if SudokuSolver.solve(board):
                    return True
                
                board[row][col] = 0 # backtrack
                
        return False
    
    # check if initial boardstate is valid
    @staticmethod
    def is_valid_board(board):
        
        for i in range(9):
            for j in range(9):
                if board[i][j] != 0:
                    num = board[i][j]
                    board[i][j] = 0 # temp remove to test
                    
                    if not SudokuSolver.is_valid(board, i, j, num):
                        board[i][j] = num # restore
                        return False
                    board[i][j] = num # restore
                    
        return True
    
    # Deep copy of board
    @staticmethod
    def copy_board(board):
        return [row[:] for row in board]
    
    
    # check if board is fully complete
    @staticmethod
    def is_complete(board):
        return SudokuSolver.find_empty(board) is None
    
    
    # count number of empty cells
    @staticmethod
    def count_empty_cells(board):
        
        count = 0
        
        for row in board:
            count += row.count(0)
            
        return count