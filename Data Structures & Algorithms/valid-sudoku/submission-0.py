class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        valid_set = set()
        for i in range(0,len(board)):
            for j in range(0,len(board[i])):
                if board[i][j] != '.':
                    row_unique = ("row",i,board[i][j])
                    if row_unique in valid_set:
                        return False
                    else:
                        valid_set.add(row_unique)
                    col_unique = ("col",j,board[i][j])
                    if col_unique in valid_set:
                        return False
                    else:
                        valid_set.add(col_unique)
                    box_unique = ("box",i//3,j//3,board[i][j])
                    if box_unique in valid_set:
                        return False
                    else:
                        valid_set.add(box_unique)
        return True
                    
                    

        