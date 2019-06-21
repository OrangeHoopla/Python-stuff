class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        column_validation = [[] for x in range(9)]
        cell_validation = [[] for x in range(9)]
        
        for row in range(len(board)):
            
            row_validation = []
            for column in range(len(board[row])):
                
                column_value = board[row][column]
                if column_value == '.':
                    continue
                
                #row validation
                if column_value not in row_validation:
                    row_validation.append(column_value)
                else:
                    return False
                
                #column valudation
                if column_value not in column_validation[column]:
                    column_validation[column].append(column_value)
                else:
                    return False
                
                #cell validation
                current_cell = 3*int(row/3) + int(column/3) 
                if column_value not in cell_validation[current_cell]:
                    cell_validation[current_cell].append(column_value)
                else:
                    return False
                
        return True
