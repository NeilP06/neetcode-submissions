class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Check rows for any potential duplicate numbers, O(n^2) work
        for row in range(len(board)):
            numbers = [False] * 9

            for col in range(len(board[0])):
                if board[row][col] == ".":
                    continue
                number = int(board[row][col])
                if numbers[number - 1]:
                    return False
                numbers[number - 1] = True

        # Check cols for any potential duplicate numbers, O(n^2) work
        for col in range(len(board[0])):
            numbers = [False] * 9

            for row in range(len(board)):
                if board[row][col] == ".":
                    continue
                number = int(board[row][col])
                if numbers[number - 1]:
                    return False
                numbers[number - 1] = True

        # Check every minigrid for any potential duplicate numbers, O(n^2) work
        for row_offset in range(0, 9, 3):
            for col_offset in range(0, 9, 3):
                numbers = [False] * 9

                for row in range(3):
                    for col in range(3):
                        if board[row + row_offset][col + col_offset] == ".":
                            continue
                        number = int(board[row + row_offset][col + col_offset])
                        if numbers[number - 1]:
                            return False
                        numbers[number - 1] = True                        

        return True