#minimax function for Tic Tac Toe, uses recursion and trees to find best possible move
#advantage - capable of searching all possible moves

def mm_move(board, player):
    """
    Make a move on the board.
    
    Returns a tuple with two elements.  The first element is the score
    of the given board and the second element is the desired move as a
    tuple, (row, col).
    """
    winner = board.check_win()
    
    if winner != None:
        return SCORES[winner], (-1, -1)
    else:
        player2 = player
        if player == provided.PLAYERX:
            player2 = provided.PLAYERO
        else:
            player2 = provided.PLAYERX  
        best_move = [SCORES[player2], (-1, -1)]
        for square in board.get_empty_squares():
            board_copy = board.clone()
            board_copy.move(square[0], square[1], player)
            returned_move = mm_move(board_copy, player2)
            score = returned_move[0]
            if player == provided.PLAYERO:
                if score < best_move[0]:
                    best_move = [score, square]
                if best_move[0] == -1:
                    return best_move[0], best_move[1]
            if player == provided.PLAYERX:
                if score > best_move[0]:
                    best_move = [score, square]
                if best_move[0] == 1:
                    return best_move[0], best_move[1]
        return best_move[0], best_move[1]