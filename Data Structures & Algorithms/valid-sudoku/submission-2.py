class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #sprawdzanie wierszy pokolei
        for row in board:
            counter = {}
            for digit in row:
                if digit == ".":
                    continue
                elif digit not in counter:
                    counter[digit] = 1
                else:
                    return False
        #sprawdzanie kolumn pokolei
        for c in range(len(board)):
            column =[]
            for r in range(len(board)):
                column.append(board[r][c])
            counter = {}
            for digit in column:
                if digit == ".":
                    continue
                elif digit not in counter:
                    counter[digit] = 1
                else:
                    return False
        #sprawdzanie kwadratów 3x3
        for br in range(3):
            for bc in range(3):
                square = []
                for r in range(br * 3, br * 3 + 3):
                    for c in range(bc * 3, bc * 3 + 3):
                        square.append(board[r][c])
                counter = {}
                for digit in square:
                    if digit == ".":
                        continue
                    elif digit not in counter:
                        counter[digit] = 1
                    else:
                        return False
        return True