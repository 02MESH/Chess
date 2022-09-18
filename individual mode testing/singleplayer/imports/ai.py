import random

piece_score = {"K": 0, "Q": 9, "R": 5, "B": 3, "N": 3, "p": 1}
"""Is a variable that is responsible for assigning a point value for
taking out each values. The AI priorities are as below;
• King is not that worthy to take out as it would be defended 
thereby having a piece_score value of 0 (low priority).
• Queen is a strong opponent so taking out a queen would make the 
AI go for the queen (high priority).
• Rook will be set to 5 (medium priority).
• Bishop will be 3 (low priority)
• Knight will be 3 (low priority)
• Pawn will be 1 (lowest priority)."""

pawn_scores = [[0.99, 0.99, 0.99, 0.99, 0.99, 0.99, 0.99, 0.99],
               [0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8],
               [0.6, 0.6, 0.7, 0.7, 0.7, 0.7, 0.6, 0.6],
               [0.4, 0.4, 0.4, 0.5, 0.5, 0.4, 0.4, 0.4],
               [0.2, 0.2, 0.2, 0.4, 0.4, 0.2, 0.2, 0.2],
               [0.25, 0.15, 0.1, 0.2, 0.2, 0.1, 0.15, 0.25],
               [0.25, 0.3, 0.3, 0.0, 0.0, 0.3, 0.3, 0.25],
               [0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2]]
"Pawn will be emphasised to move forward to get more pieces i.e. the queen."
knight_scores = [[0.0, 0.1, 0.2, 0.2, 0.2, 0.2, 0.1, 0.0],
                 [0.1, 0.3, 0.5, 0.5, 0.5, 0.5, 0.3, 0.1],
                 [0.2, 0.5, 0.6, 0.65, 0.65, 0.6, 0.5, 0.2],
                 [0.2, 0.55, 0.65, 0.9, 0.9, 0.65, 0.55, 0.2],
                 [0.2, 0.5, 0.65, 0.9, 0.9, 0.65, 0.5, 0.2],
                 [0.2, 0.55, 0.6, 0.65, 0.65, 0.6, 0.55, 0.2],
                 [0.1, 0.3, 0.5, 0.55, 0.55, 0.5, 0.3, 0.1],
                 [0.0, 0.1, 0.2, 0.2, 0.2, 0.2, 0.1, 0.0]]
"Knights will be emphasied to be in the middle as it will the strongest there."
rook_scores = [[0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25],
               [0.5, 0.75, 0.75, 0.75, 0.75, 0.75, 0.75, 0.5],
               [0.0, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.0],
               [0.0, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.0],
               [0.0, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.0],
               [0.0, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.0],
               [0.0, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.0],
               [0.25, 0.25, 0.25, 0.5, 0.5, 0.25, 0.25, 0.25]]
"Rooks will be best at the edges of the chess board."





bishop_scores = [[0.0, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.0],
                 [0.2, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.2],
                 [0.2, 0.4, 0.5, 0.6, 0.6, 0.5, 0.4, 0.2],
                 [0.2, 0.5, 0.5, 0.6, 0.6, 0.5, 0.5, 0.2],
                 [0.2, 0.4, 0.6, 0.6, 0.6, 0.6, 0.4, 0.2],
                 [0.2, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.2],
                 [0.2, 0.5, 0.4, 0.4, 0.4, 0.4, 0.5, 0.2],
                 [0.0, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.0]]
"Bishops will be best at the mid section of the chess board."
queen_scores = [[0.0, 0.2, 0.2, 0.3, 0.3, 0.2, 0.2, 0.0],
                [0.2, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.2],
                [0.2, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.2],
                [0.3, 0.4, 0.5, 0.7, 0.7, 0.5, 0.4, 0.3],
                [0.3, 0.4, 0.5, 0.6, 0.6, 0.5, 0.4, 0.3],
                [0.2, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.2],
                [0.2, 0.4, 0.5, 0.4, 0.4, 0.4, 0.4, 0.2],
                [0.0, 0.2, 0.2, 0.3, 0.3, 0.2, 0.2, 0.0]]
"Queen will be generally be the most powerful piece if in the middle."
"""Saved in these list are the scores which will give the AI points for moving the 
pieces to going to the designated destination which will make it stronger. For instance, if
the AI finds that if another location has more points than the current location, it will 
move the piece to the designated places."""


piece_position_scores = {"wN": knight_scores,
                         "bN": knight_scores[::-1],
                         "wB": bishop_scores,
                         "bB": bishop_scores[::-1],
                         "wQ": queen_scores,
                         "bQ": queen_scores[::-1],
                         "wR": rook_scores,
                         "bR": rook_scores[::-1],
                         "wp": pawn_scores,
                         "bp": pawn_scores[::-1]}

CHECKMATE = 1000
"Priority to get a checkmate will be set to 1000"
STALEMATE = 0
"Priority to get a stalemate will be set to 0"
DEPTH = 3
"""Variable that stores the constant 3 specifying the negamax algorithm
depth i.e. the AI will reduce possibilities up to 3 moves. Whichever move
has the highest value. It will be executed.
The more the depth, the slower the ai will think."""


def findBestMove(game_state, valid_moves, return_queue):
    "Subroutine that will act as the main subroutine for the ai.py file."
    "It will be called in the main.py file."
    global next_move
    next_move = None
    random.shuffle(valid_moves)
    findMoveNegamaxAlphaBeta(game_state, valid_moves, DEPTH, -CHECKMATE, CHECKMATE,
                             1 if game_state.white_to_move else -1)
    return_queue.put(next_move)


def findMoveNegamaxAlphaBeta(game_state, valid_moves, depth, alpha, beta, turn_multiplier):
    """Greedy fashion. We will be looking at all the moves and find the best available move.
    It will also include alpha beta pruning, the idea is as we are going through the game tree,
    at some state, if we find that if we are making a move, they may counter with a move which
    result in the AI losing it. Rather than going through the recursion depth, we just eliminate
    the game tree search."""
    "When alpha becomes equal to beta, we break out of the loop."
    global next_move
    if depth == 0:
        return turn_multiplier * scoreBoard(game_state)
    max_score = -CHECKMATE
    "Score being negative CHECKMATE"
    for move in valid_moves:
        "For move in the number of valid moves."
        game_state.makeMove(move)
        "Making the move"
        next_moves = game_state.moveValidation()
        "Validate the move"
        score = -findMoveNegamaxAlphaBeta(game_state, next_moves, depth - 1, -beta, -alpha, -turn_multiplier)
        if score > max_score:
            "If the score exceeds the max_score"
            max_score = score
            "max_score will be set to score. It will make the maximise the best move potential."
            if depth == DEPTH:
                "After the depth has been reached i.e. 3"
                next_move = move
                "next_move will be set to move."
        game_state.undoMove()
        if max_score > alpha:
            "If the max score is already greater than alpha, it becomes our new alpha value."
            alpha = max_score
        if alpha >= beta:
            "When alpha becomes equal to beta, we break out of the loop."
            break
    return max_score


def scoreBoard(game_state):
    """Subroutine that scores moves. Where there is a  positive for white, and a negative score
    for black."""
    if game_state.checkmate:
        if game_state.white_to_move:
            return -CHECKMATE
            #black wins here
        else:
            return CHECKMATE
            #White wins here
    elif game_state.stalemate:
        return STALEMATE
    score = 0
    for row in range(len(game_state.board)):
        for columns in range(len(game_state.board[row])):
            piece = game_state.board[row][columns]
            if piece != "--":
                "If the box is empty."
                piece_position_score = 0
                if piece[1] != "K":
                    piece_position_score = piece_position_scores[piece][row][columns]
                if piece[0] == "w":
                    "If the piece is a white piece, we will add the score."
                    score += piece_score[piece[1]] + piece_position_score
                if piece[0] == "b":
                    "If the piece is a black piece, will will subtract the score."
                    score -= piece_score[piece[1]] + piece_position_score

    return score


def findRandomMove(valid_moves):
    """Calls the random.choice subroutine with valid move generation."""
    return random.choice(valid_moves)

import random

piece_score = {"K": 0, "Q": 9, "R": 5, "B": 3, "N": 3, "p": 1}
"""Is a variable that is responsible for assigning a point value for
taking out each values. The AI priorities are as below;
• King is not that worthy to take out as it would be defended 
thereby having a piece_score value of 0 (low priority).
• Queen is a strong opponent so taking out a queen would make the 
AI go for the queen (high priority).
• Rook will be set to 5 (medium priority).
• Bishop will be 3 (low priority)
• Knight will be 3 (low priority)
• Pawn will be 1 (lowest priority)."""

pawn_scores = [[0.99, 0.99, 0.99, 0.99, 0.99, 0.99, 0.99, 0.99],
               [0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8],
               [0.6, 0.6, 0.7, 0.7, 0.7, 0.7, 0.6, 0.6],
               [0.4, 0.4, 0.4, 0.5, 0.5, 0.4, 0.4, 0.4],
               [0.2, 0.2, 0.2, 0.4, 0.4, 0.2, 0.2, 0.2],
               [0.25, 0.15, 0.1, 0.2, 0.2, 0.1, 0.15, 0.25],
               [0.25, 0.3, 0.3, 0.0, 0.0, 0.3, 0.3, 0.25],
               [0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2]]
"Pawn will be emphasised to move forward to get more pieces i.e. the queen."
knight_scores = [[0.0, 0.1, 0.2, 0.2, 0.2, 0.2, 0.1, 0.0],
                 [0.1, 0.3, 0.5, 0.5, 0.5, 0.5, 0.3, 0.1],
                 [0.2, 0.5, 0.6, 0.65, 0.65, 0.6, 0.5, 0.2],
                 [0.2, 0.55, 0.65, 0.9, 0.9, 0.65, 0.55, 0.2],
                 [0.2, 0.5, 0.65, 0.9, 0.9, 0.65, 0.5, 0.2],
                 [0.2, 0.55, 0.6, 0.65, 0.65, 0.6, 0.55, 0.2],
                 [0.1, 0.3, 0.5, 0.55, 0.55, 0.5, 0.3, 0.1],
                 [0.0, 0.1, 0.2, 0.2, 0.2, 0.2, 0.1, 0.0]]
"Knights will be emphasied to be in the middle as it will the strongest there."
rook_scores = [[0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25],
               [0.5, 0.75, 0.75, 0.75, 0.75, 0.75, 0.75, 0.5],
               [0.0, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.0],
               [0.0, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.0],
               [0.0, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.0],
               [0.0, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.0],
               [0.0, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.0],
               [0.25, 0.25, 0.25, 0.5, 0.5, 0.25, 0.25, 0.25]]
"Rooks will be best at the edges of the chess board."





bishop_scores = [[0.0, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.0],
                 [0.2, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.2],
                 [0.2, 0.4, 0.5, 0.6, 0.6, 0.5, 0.4, 0.2],
                 [0.2, 0.5, 0.5, 0.6, 0.6, 0.5, 0.5, 0.2],
                 [0.2, 0.4, 0.6, 0.6, 0.6, 0.6, 0.4, 0.2],
                 [0.2, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.2],
                 [0.2, 0.5, 0.4, 0.4, 0.4, 0.4, 0.5, 0.2],
                 [0.0, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.0]]
"Bishops will be best at the mid section of the chess board."
queen_scores = [[0.0, 0.2, 0.2, 0.3, 0.3, 0.2, 0.2, 0.0],
                [0.2, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.2],
                [0.2, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.2],
                [0.3, 0.4, 0.5, 0.7, 0.7, 0.5, 0.4, 0.3],
                [0.3, 0.4, 0.5, 0.6, 0.6, 0.5, 0.4, 0.3],
                [0.2, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.2],
                [0.2, 0.4, 0.5, 0.4, 0.4, 0.4, 0.4, 0.2],
                [0.0, 0.2, 0.2, 0.3, 0.3, 0.2, 0.2, 0.0]]
"Queen will be generally be the most powerful piece if in the middle."
"""Saved in these list are the scores which will give the AI points for moving the 
pieces to going to the designated destination which will make it stronger. For instance, if
the AI finds that if another location has more points than the current location, it will 
move the piece to the designated places."""


piece_position_scores = {"wN": knight_scores,
                         "bN": knight_scores[::-1],
                         "wB": bishop_scores,
                         "bB": bishop_scores[::-1],
                         "wQ": queen_scores,
                         "bQ": queen_scores[::-1],
                         "wR": rook_scores,
                         "bR": rook_scores[::-1],
                         "wp": pawn_scores,
                         "bp": pawn_scores[::-1]}

CHECKMATE = 1000
"Priority to get a checkmate will be set to 1000"
STALEMATE = 0
"Priority to get a stalemate will be set to 0"
DEPTH = 3
"""Variable that stores the constant 3 specifying the negamax algorithm
depth i.e. the AI will reduce possibilities up to 3 moves. Whichever move
has the highest value. It will be executed.
The more the depth, the slower the ai will think."""


def findBestMove(game_state, valid_moves, return_queue):
    "Subroutine that will act as the main subroutine for the ai.py file."
    "It will be called in the main.py file."
    global next_move
    next_move = None
    random.shuffle(valid_moves)
    findMoveNegamaxAlphaBeta(game_state, valid_moves, DEPTH, -CHECKMATE, CHECKMATE,
                             1 if game_state.white_to_move else -1)
    return_queue.put(next_move)


def findMoveNegamaxAlphaBeta(game_state, valid_moves, depth, alpha, beta, turn_multiplier):
    """Greedy fashion. We will be looking at all the moves and find the best available move.
    It will also include alpha beta pruning, the idea is as we are going through the game tree,
    at some state, if we find that if we are making a move, they may counter with a move which
    result in the AI losing it. Rather than going through the recursion depth, we just eliminate
    the game tree search."""
    "When alpha becomes equal to beta, we break out of the loop."
    global next_move
    if depth == 0:
        return turn_multiplier * scoreBoard(game_state)
    max_score = -CHECKMATE
    "Score being negative CHECKMATE"
    for move in valid_moves:
        "For move in the number of valid moves."
        game_state.makeMove(move)
        "Making the move"
        next_moves = game_state.moveValidation()
        "Validate the move"
        score = -findMoveNegamaxAlphaBeta(game_state, next_moves, depth - 1, -beta, -alpha, -turn_multiplier)
        if score > max_score:
            "If the score exceeds the max_score"
            max_score = score
            "max_score will be set to score. It will make the maximise the best move potential."
            if depth == DEPTH:
                "After the depth has been reached i.e. 3"
                next_move = move
                "next_move will be set to move."
        game_state.undoMove()
        if max_score > alpha:
            "If the max score is already greater than alpha, it becomes our new alpha value."
            alpha = max_score
        if alpha >= beta:
            "When alpha becomes equal to beta, we break out of the loop."
            break
    return max_score


def scoreBoard(game_state):
    """Subroutine that scores moves. Where there is a  positive for white, and a negative score
    for black."""
    if game_state.checkmate:
        if game_state.white_to_move:
            return -CHECKMATE
            #black wins here
        else:
            return CHECKMATE
            #White wins here
    elif game_state.stalemate:
        return STALEMATE
    score = 0
    for row in range(len(game_state.board)):
        for columns in range(len(game_state.board[row])):
            piece = game_state.board[row][columns]
            if piece != "--":
                "If the box is empty."
                piece_position_score = 0
                if piece[1] != "K":
                    piece_position_score = piece_position_scores[piece][row][columns]
                if piece[0] == "w":
                    "If the piece is a white piece, we will add the score."
                    score += piece_score[piece[1]] + piece_position_score
                if piece[0] == "b":
                    "If the piece is a black piece, will will subtract the score."
                    score -= piece_score[piece[1]] + piece_position_score

    return score


def findRandomMove(valid_moves):
    """Calls the random.choice subroutine with valid move generation."""
    return random.choice(valid_moves)

