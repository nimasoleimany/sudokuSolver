
import itertools
from time import sleep
def check_board(sudoku_board):

    def row_checker(board):
        for i in range(len(board)):
             if sum(set(board[i]))!= sum(board[i]):
                 return False
        return True

    def column_checker(board):
        transpose = [[board[j][i] for j in range(len(board))] for i in range(len(board))]
        for i in range(len(transpose)):
             if sum(set(transpose[i]))!= sum(transpose[i]):
                 return False
        return True

    def sub_grid_checker(board):
        squares = []
        for i in range(0 , 9 , 3):
            for j in range(0 , 9 ,3):
                sub_grid = list(itertools.chain(row[j:j+3] for row in board[i:i+3]))
                squares.append(sub_grid)
        for square in squares : 
            if sum(set(itertools.chain.from_iterable(square))) != sum(list(itertools.chain.from_iterable(square))) : 
                return False
        return True
 
    return row_checker(sudoku_board) and column_checker(sudoku_board) and sub_grid_checker(sudoku_board) 

def solver(sudoku):

    def find_empty_location(board):
        for row in range(len(board)):
            for column in range(len(board)):
                if board[row][column] == 0 :
                    return row, column
        return False

    def row_checker(board ,row ,column ,number):
        for i in range(len(board)):
            if board[row][i] == number and column != i :
                return True
        return False

    def column_checker(board ,row ,column ,number):
        for i in range (len(board)):
            if board[i][column] == number and row != i :
                return True
        return False

    def sub_grid_checker(board ,row , column ,number):
        for i in range((row // 3 )* 3 , (row // 3 ) * 3 + 3 ):
            for j in range((column // 3 )* 3 , (column // 3 ) *3 + 3 ):
                if board[i][j] == number and (i , j) != (row , column) : 
                    return True
        return False

    def is_feasibile(board ,row ,column ,number):
        return not row_checker(board ,row ,column ,number) and not column_checker(board ,row ,column ,number) and not sub_grid_checker(board ,row ,column ,number)

    def solve_sudoku(board):
        cordinates = find_empty_location(board)
        if not cordinates :
            return True
        row, column = cordinates 
        for number in range(1 ,10): 
            if is_feasibile(board ,row ,column ,number):
                board[row][column] = number 
                if solve_sudoku(board):
                    return True
                board[row][column] = 0
        return False
    if solve_sudoku(sudoku) is True : 
        return sudoku
    return False

def show_board(board):
    print("-" * 37)
    for i, row in enumerate(board):
        print(("|"+" {}   {}   {}  |" * 3).format(*[str(x) if x !=0 else " " for x in row]))
        if (i, row) == (8, row):
            print("-" * 37)
            if i % 3 == 2 and i != 8 :
                print("+" + "---+" * 9 )
            if i % 3 != 2 and i != 8 :
                print("|    "+ "+   " * 8 + "|")

##--[SOLVE]
sudoku_tabel = [[0, 0, 0, 0, 0, 0, 0, 1, 0],
                [0, 0, 0, 0, 0, 2, 0, 0, 3],
                [0, 0, 0, 4, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 5, 0, 0],
                [6, 0, 1, 7, 0, 0, 0, 0, 0],
                [0, 0, 4, 1, 0, 0, 0, 0, 0],
                [0, 5, 0, 0, 0, 0, 7, 0, 0],
                [0, 0, 0, 0, 8, 0, 0, 6, 0],
                [0, 3, 0, 9, 1, 0, 0, 0, 0]]

print("Very well \n this is your sudoku : " + "\n")
show_board(sudoku_tabel)
sleep(5)
print("Now Python solves your sudoku : \n ")
solution = solver(sudoku_tabel)
show_board(solution)
print("is written by Nima SOleimani  \n Telegram id = [ @Nimaw_org ]\n")