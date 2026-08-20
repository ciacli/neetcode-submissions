
class Solution:
    def valid_config(self, line, column, freq, board):
        string = board[line][column]
        if string == ".":
            return True
        elem = ord(string) - ord('0')
        if freq[elem] == 1:
            print(str(line) + ' ' + str(column))
            return False
        if elem < 1:
            print(str(line) + ' ' + str(column))
            return False
        freq[elem] = 1
        return True
    
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #valid lines
        for line in range(0, 9):
            freq = [0] * 10
            for column in range(0, 9):
                if self.valid_config(line, column, freq, board) == False:
                    return False
                
        
        #valid columns
        for column in range(0, 9):
            freq = [0] * 10
            for line in range(0, 9):
                if self.valid_config(line, column, freq, board) == False:
                    return False
        
        #valid squares
        for y in range(0, 3):
            for x in range(0, 3):
                freq = [0] * 10
                for line in range(y * 3, (y + 1) * 3):
                    for column in range(x * 3, (x + 1) * 3):
                        if self.valid_config(line, column, freq, board) == False:
                            return False
        return True



