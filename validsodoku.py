class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        n = len(board)

        for i in range(n):

            seen = set()

            for j in range(n):

                cell = board[i][j]

                if cell == ".":
                    continue

                if cell in seen:
                    return False

                seen.add(cell)

        for j in range(n):

            seen = set()

            for i in range(n):

                cell = board[i][j]

                if cell == ".":
                    continue

                if cell in seen:
                    return False

                seen.add(cell)

        for boxRow in range(0, n, 3):

            for boxCol in range(0, n, 3):

                seen = set()

                for i in range(boxRow, boxRow + 3):

                    for j in range(boxCol, boxCol + 3):

                        cell = board[i][j]

                        if cell == ".":
                            continue

                        if cell in seen:
                            return False

                        seen.add(cell)

        return True