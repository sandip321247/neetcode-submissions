class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        columns = len(board[0])
        lengthOfWord = len(word)

        if rows == 1 and columns == 1:
            return board[0][0] == word

        def backtrack(position , index):
            i , j = position

            if index == lengthOfWord:
                return True

            if board[i][j] != word[index]:
                return False
            
            tempVariable = board[i][j]
            board[i][j] = '#' #to ensure i would not repeat

            for i_off , j_off in [(0,1),(1,0),(-1,0),(0,-1)]:
                r , c = i + i_off , j + j_off
                if 0 <= r < rows and 0 <= c < columns:
                    if backtrack((r , c) , index+1):
                        return True

            board[i][j] = tempVariable
            return False

        for i in range(rows):
            for j in range(columns):
                if backtrack((i,j),0):
                    return True

        return False
