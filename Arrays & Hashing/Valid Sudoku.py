class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #check Rows
        for board_row in range(len(board)):
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
        

        return True
