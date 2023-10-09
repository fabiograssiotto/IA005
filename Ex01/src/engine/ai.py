
class AI:
    def __init__(self) -> None:
        pass

    # Main Play Function
    def play(self, board):
        # Min-Max algorithm.
        bestEval = -1000 # evaluation
        bestMove = (-1, -1) # movement

        # Board search for the best move for the second player.
        for line in range(3):
            for col in range(3):
                if (board[line][col] == 0):
                    # position available
                    board[line][col] = 2
                    eval = self.miniMax(board, 0, False)
                    # reset move
                    board[line][col] = 0
                    # Was this the best move?
                    if (eval > bestEval):
                        bestMove = (line, col)
                        bestEval = eval
        return bestMove

    # Minimax algorithm
    def miniMax(self, board, depth, maxMove):
        # First evaluate board score
        myScore = self.evaluateBoard(board)
        # Maximizer won the game
        if (myScore == 10):
            return myScore
        # Minimizer won the game
        if (myScore == -10):
            return myScore
        # Draw
        if (self.anyMovesLeft(board) == False):
            return 0

        # Maximizer move
        if (maxMove):
            bestMove = -1000
            for line in range(3):
                for col in range(3):
                    if (board[line][col] == 0):
                        # make the move
                        board[line][col] = 2
                        # Recursively find the best move possible
                        bestMove = max(bestMove, self.miniMax(board, depth+1, not maxMove))
                        board[line][col] = 0
            return bestMove
        # Minimizer move
        else:
            bestMove = 1000
            for line in range(3):
                for col in range(3):
                    if (board[line][col] == 0):
                        # make the move
                        board[line][col] = 1
                        # Recursively find the worst move possible (for the opponent)
                        bestMove = min(bestMove, self.miniMax(board, depth+1, not maxMove))
                        board[line][col] = 0
            return bestMove

    # Evaluation function
    def evaluateBoard(self, board):
        eval = 0
        # Check rows
        for row in range(3):
            if (board[row][0] == board[row][1] and board[row][1] == board[row][2]):
                if (board[row][0] == 1):
                    eval = -10
                    return eval
                elif (board[row][0] == 2):
                    eval = 10
                    return eval        
        # Check cols
        for col in range(3):
            if (board[0][col] == board[1][col] and board[1][col] == board[2][col]):
                if (board[0][col] == 1):
                    eval = -10
                    return eval
                elif (board[0][col] == 2):
                    eval = 10
                    return eval
        # Check diags
        if (board[0][0] == board[1][1] and board[1][1] == board[2][2]):
            if (board[0][0] == 1):
                eval = -10
                return eval
            elif (board[0][0] == 2):
                eval = 10
                return eval            
        if (board[0][2] == board[1][1] and board[1][1] == board[2][0]):
            if (board[0][2] == 1):
                eval = -10
                return eval
            elif (board[0][2] == 2):
                eval = 10
                return eval
        
        # in all other cases return default value = 0
        return eval
    
    # Any Moves left
    def anyMovesLeft(self, board) :  
        for line in range(3) : 
            for col in range(3) : 
                if (board[line][col] == 0) : 
                    return True 
        return False