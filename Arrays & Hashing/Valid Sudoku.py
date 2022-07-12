class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #check Rows
        for board_row in range(9):
            seen_nums = []
            for sub_num in board[board_row]:
                if sub_num not in seen_nums and sub_num != ".":
                    seen_nums.append(sub_num)
                elif sub_num == ".":
                    continue
                else: 
                    return False

        #Check columns 
        for current_column in range(9):
            seen_nums = []
            for current_row in range(9):
                if (board[current_row][current_column] not in seen_nums) and (board[current_row][current_column] != "."):
                    seen_nums.append(board[current_row][current_column])
                elif board[current_row][current_column] == ".":
                    continue
                else: 
                    return False
                
        #Check Squares
        for row_mod in range(0, 9, 3):
            for col_mod in range(0, 9, 3):
                seen_nums = []
                for small_column in range(0+col_mod,3+col_mod):
                    for small_rows in range(0+row_mod, 3+row_mod):
                        if (board[small_rows][small_column] not in seen_nums) and (board[small_rows][small_column] != "."):
                            seen_nums.append(board[small_rows][small_column])
                        elif board[small_rows][small_column] == ".":
                            continue
                        else: 
                            return False

        return True


