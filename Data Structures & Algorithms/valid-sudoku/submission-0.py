class Solution:

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        def isValid(row: list[str]) -> bool: 
            seen = {}
            for elem in row:
                if elem in seen.keys() and elem != '.':
                    print(f"row: {row}, elem: {elem}")
                    return False 
                else:
                    seen[elem] = 1
            return True

        flats = [[board[r+i][c+j] for i in range(3) for j in range(3)] #3x3 boxes into a matrix
         for r in range(0, 9, 3) for c in range(0, 9, 3)]
        print(f"3x3's flats: {flats}")

        transposed = [list(row) for row in zip(*board)] # columns into a matrix
        print(f"columns : {transposed}")

        for x in range(9):
            isRowValid = isValid(board[x])
            print(f"IsRowValid = {isRowValid}")
            isColValid = isValid(transposed[x])
            print(f"isColValid = {isColValid}")
            isBoxValid = isValid(flats[x])
            print(f"isBoxValid = {isBoxValid}")
           
            if not (isRowValid and isColValid and isBoxValid):
                print(f"row: {board[x]}")
                print(f"col: {transposed[x]}")
                print(f"3x3: {flats[x]}")
                return False
        return True
