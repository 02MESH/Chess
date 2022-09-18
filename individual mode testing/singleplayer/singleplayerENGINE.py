import pygame as p
from imports import board as b
from imports import ai
from imports import piece as pie
import sys
from multiprocessing import Process, Queue

####################################
boardDIMENSION = 8                 #
width = height = 500               #
BOX_SIZE = height // boardDIMENSION#
moveTURNwidth = 200                #
FPS = 60                           #
rendered = pie.rendered            #
####################################
p.init()


def playGame():
    screen = p.display.set_mode((width + moveTURNwidth, height))
    clock = p.time.Clock()
    screen.fill((0,0,0))
    gs = b.piece_manager()
    validate = gs.moveValidation()
    """
    • Screen is declared as a variable which will be used to set the display specified 
    by the global variable dimension i.e. width and height.
    • Clock is an important variable where it will be used to animate the piece when 
    they are moved by the user. 
    • screen.fill basically fills the screen with black, i.e. specified by the RGB 
    values (0,0,0).
    • gs is basically a call saved in engine.py which calls the class from board.py 
    which is GameState.
    • validate is a call saved in engine.py which calls the class from board i.e. 
    moveValidation().
    """


    moveMADE = False
    animations = False
    pie.RenderImage()
    running = True
    square_selected = ()
    clicked = []
    game_over = False
    aiProcess = False
    move_undone = False
    move_finder_process = None
    player_one = True
    player_two = False
    """
    • moveMADE is a flag variable which is set and will change as moves are made.
    • animations is a flag variable which will turn True whenever the animateMoves
    subroutine is called that will then animate the piece transition.
    • pie.RenderImage() we initialise the subroutine def RenderImage from the 
    piece.py library which initialises the process of rendering the pictures
    according to the dimension. It will be passed from piece.py.
    • running is a flag variable that will change after the game finishes. It's the
    idea of an infinite loop that will continuously run the game.
    • square_selected tracks user clicks and saves it in a tuple.
    • clicked saves the clicks data of the user when clicked at a square on the 
    chess board.
    • game_over is a flag variables that triggers after the game is over.
    • aiProcess is a flag variable that is set to pass the command to the AI.
    • move_undone is a flag variable to check whether the user has undone a 
    move.
    • move_finder_process is a set to None.
    • player_one is a flag variable which is set which will be true for the first 
    player otherwise false for the AI. player_two is a similar flag variable that 
    is set that will pass the command to the AI.
    """

    while running: # Infinite loop that will run def main():
        "The flag variable running being called that will run the loop."
        human_turn = (gs.white_to_move and player_one) or (not gs.white_to_move and player_two)
        "An ADD operation where the results are saved in a variable named human_turn."

        for event in p.event.get():
            "For every event in the pygame library."

            if event.type == p.QUIT:
                "If the event type is pygame.QUIT"
                p.quit()
                sys.exit()
                #"Pygame and system exiting."

            elif event.type == p.MOUSEBUTTONDOWN:
                "Part of the code when the user clicks a mouse button."

                if not game_over:
                    location = p.mouse.get_pos()  # Holds the location of the mouse.
                    column = location[0] // BOX_SIZE
                    row = location[1] // BOX_SIZE
                    "• location holds the position of the mouse."

                    if square_selected == (row, column) or column >= 8:
                        square_selected = ()
                        clicked = []
                        """
                        If the user clicks a location which doesn't have to do anything 
                        with the game, clicked and square_selected will be set to empty."""

                    else:
                        square_selected = (row, column)
                        clicked.append(square_selected)
                        """
                        If the user has clicked on the piece and then clicks on where they
                        want to move it. It will append the move in the clicked tuple.
                        """

                    if len(clicked) == 2 and human_turn:
                        move = b.Move(clicked[0], clicked[1], gs.board)
                        "Occurring after the second click and if the human is playing."

                        for i in range(len(validate)):
                            """
                            Loop that will execute to the number of contents in validate
                            i.e. validation subroutine in board.py.
                            """


                            if move == validate[i]:
                                "If the move matches the requirements in the validate library."

                                gs.makeMove(validate[i])
                                moveMADE = True
                                animations = True
                                square_selected = ()
                                clicked = []
                                """
                                Variables being set to true if the move matches the validate 
                                requirements."""

                        if not moveMADE:
                            clicked = [square_selected]
                            "Error handling in case the user has not made any move."

            elif event.type == p.KEYDOWN:
                "Part of the code when pygame finds after it discovers a keyboard button click."

                if event.key == p.K_z:
                    "If the button click is z"
                    gs.undoMove()
                    "It will call the subroutine from board.py which is undoMove()"
                    moveMADE = True
                    animations = False
                    game_over = False
                    """
                    • moveMADE will be set to True as the user will get to play again.
                    • animations will be False as it will have to redo as the user
                    has undone the move.
                    • game_over will be set back to false even if the the end message
                    is displayed."""

                    if aiProcess:
                        "If ai Process is True"
                        move_finder_process.terminate()
                        "Start executing move_finder_process.terminate() to find the move."
                        aiProcess = False
                        "aiProcess will be set back to false then."
                    move_undone = True
                    "move_undone will be set back to True."

                if event.key == p.K_ESCAPE:
                    "If the user enters the escape key"
                    p.display.set_mode((width, height))
                    "It will produce a pane for the mainGUI.py to continue."
                    running = False
                    "Will stop the loop execution."

                if event.key == p.K_r:
                    "If the keyboard button r is pressed."
                    gs = b.piece_manager()
                    "Defines the gamestate class from board.py in engine.py."
                    validate = gs.moveValidation()
                    "Defines the moveValidation class from board.py in engine.py."
                    square_selected = ()
                    clicked = []
                    """
                    • square_selected i.e. the tuple will be set back to empty.
                    • The clicked list will also be set back to an empty list."""
                    moveMADE = False
                    animations = False
                    game_over = False
                    """
                    • moveMade will be False i.e. the user will get to start again.
                    • animations will be false as the user has to make a move and then the
                    code will start again with the animation.
                    • if the game was previously over, it would be set back to false."""

                    if aiProcess:
                        """If the aiProcess variable is True, then this part of the code 
                        will start executing."""

                        move_finder_process.terminate()
                        aiProcess = False
                        """
                        • move_finder process.terminate will begin.
                        • after the AI has played, it will set it back to False for the user's move."""
                    move_undone = True
                    "If aiProcess is not True, move_undone will be False"


        if not game_over and not human_turn and not move_undone:
            "Boolean selection statement used if requirements met."

            if not aiProcess:
                "if aiProcess if False"
                aiProcess = True
                "aiProcess will be set to True"
                return_queue = Queue()
                move_finder_process = Process(target=ai.findBestMove, args=(gs, validate, return_queue))
                move_finder_process.start()
                """This will initiate the move finding process which imports from the ai.py 
                and will validate it with the validate subroutine from the board.py file."""

            if not move_finder_process.is_alive():
                "If not move_finder_process is False, this will activate this part."

                ai_move = return_queue.get()

                if ai_move is None:
                    ai_move = ai.findRandomMove(validate)
                    "If the AI doesn't find any relevant moves, it will start generating random moves."
                gs.makeMove(ai_move)
                "Start executing makeMove from the ai.py file."
                moveMADE = True
                animations = True
                aiProcess = False
                "Variables start changing for the ai to perform."

        if moveMADE:
            "If moveMADE is True"

            if animations:
                "If animations is True, it will start producing the animations"
                animateMove(gs.moveRegister[-1], screen, gs.board, clock)
                "Piece animation begins"
            validate = gs.moveValidation()
            "Move validation"
            moveMADE = False
            animations = False
            move_undone = False
            "Key variables change to facilitate change."

        drawGameState(screen, gs, validate, square_selected)
        "Starts drawing the game board with the pieces and whose turn it is."

        if gs.checkmate:
            "if the program finds the game is in checkmate."
            game_over = True
            "game_over will be set to True"

            if gs.white_to_move:
                "If gs.white_to_move is True, this part will execute."
                drawEndGameText(screen, "BLACK WINS THE GAME BY CHECKMATE")
                """will draw the text on the screen that the game is over 
                by checkmate by black."""
            else:
                drawEndGameText(screen, "WHITE WINS THE GAME BY CHECKMATE")
                """will draw the text on the screen that the game is over 
                   by checkmate by white."""


        elif gs.stalemate:
            "if the program finds the game is in a stalemate"
            game_over = True
            "game_over will be set to True"
            drawEndGameText(screen, "STALEMATE")
            """will draw the text on the screen that the game is over by
            stalemate any of the pieces."""


        clock.tick(FPS)
        p.display.flip()
        """
        • The clock will start ticking which will start FPS count, i.e. run the loop
        on 60 frames.
        • display.flip will update the contents of the entire display."""


def drawGameState(screen, gs, valid_moves, square_selected):

    "Imports arguments that holds information to construct the board."
    drawBoard(screen)
    "#draw squares on the board"
    highlightSquares(screen, gs, valid_moves, square_selected)
    "highlight squares on the board"
    drawPieces(screen, gs.board)
    "# draw pieces on top of those squares"
    drawTurn(screen, gs)
    "Subroutine that draw whose turn it is."


def drawBoard(screen):
    "Imports arguments that holds data to construct the squares."
    global colors
    "Imports colors which don't require pygame to type RGB values."
    colors = [p.Color("grey"), p.Color("darkcyan")]
    "List that saves the colours for the variable BOX_SQUARE"
    for row in range(boardDIMENSION):
        "for loop that will draw the 2D array i.e. the chess board."
        for column in range(boardDIMENSION):
            "# for loop that will partition the board which will result in 64 squares."
            color = colors[((row + column) % 2)]
            "# Board will be equal to the chess board pattern. Chequered squares."
            p.draw.rect(screen, color, p.Rect(column * BOX_SIZE, row * BOX_SIZE, BOX_SIZE, BOX_SIZE))
            "# Draw the boxes."


def highlightSquares(screen, gs, valid_moves, square_selected):
    "Part of the game that will handle the highlighting of the chess pieces."
    if (len(gs.moveRegister)) > 0:
        "If the length of the moveRegister in the board.py file is greater than 0."
        last_move = gs.moveRegister[-1]
        s = p.Surface((BOX_SIZE, BOX_SIZE))
        s.set_alpha(100)
        s.fill(p.Color('green'))
        """after the piece has reached its location, it will highlight
        the square green."""
        screen.blit(s, (last_move.end_col * BOX_SIZE, last_move.end_row * BOX_SIZE))
        "producing the highlight."

    if square_selected != ():
        "if the square_selected tuple is not empty."
        row, col = square_selected
        "row, column will be equal to square_selected as it will highlight."

        if gs.board[row][col][0] == (

                'w' if gs.white_to_move else 'b'):

            "square_selected is a piece that can be moved"
            "highlight selected square"
            s = p.Surface((BOX_SIZE, BOX_SIZE))
            s.set_alpha(100)
            "transparency value 0 -> transparent, 255 -> opaque"
            s.fill(p.Color('blue'))
            screen.blit(s, (col * BOX_SIZE, row * BOX_SIZE))
            "highlight moves from that square"
            s.fill(p.Color('yellow'))

            for move in valid_moves:
                "for the number of moves in valid_moves"
                if move.start_row == row and move.start_col == col:
                    "if the move.start_row is equal to the column"
                    screen.blit(s, (move.end_col * BOX_SIZE, move.end_row * BOX_SIZE))
                    """on the specific row and column the screen will be blit,
                    the highlight will be drawn."""


# Code that will fit the chess piece image on the board.
def drawPieces(screen, board):
    "Subroutine that will print the chess pieces on the board."

    for row in range(boardDIMENSION):
        "for i in boardDimension i.e. 8 because 64 boxes on board"
        for column in range(boardDIMENSION):
            "for j in boardDimension i.e. 8 because 64 boxes on board"
            piece = board[row][column]
            "saving the board rows and columns in a variable named piece"
            if piece != "--":
                "if piece is empty, then it will leave that space empty"
                screen.blit(rendered[piece], p.Rect(column * BOX_SIZE, row * BOX_SIZE, BOX_SIZE, BOX_SIZE))
                "finally render the images on the board."


def drawTurn(screen, gs):
    "Subroutine that will manufacture whose turn it on the singleENGINE pane"
    white = p.image.load('resources/' + 'white.jpg')
    black = p.image.load('resources/' + 'black.jpg')
    "Loads the pictures"

    playerFont = p.font.SysFont("Aleo", 35)
    box1 = p.Rect((525, 100), (150, 100))
    box2 = p.Rect((525, 300), (150, 100))
    player1 = playerFont.render("YOUR TURN", True, p.Color("black"))
    player2 = playerFont.render("COMPUTER", True, p.Color("black"))
    highlightP1 = p.Rect((515, 90), (170, 120))
    highlightP2 = p.Rect((515, 290), (170, 120))
    """Varibles that holds vital information to produce the text and rectangles
    on the singleENGINE pane."""

    if gs.white_to_move:
        """This needs to produced first since other rectangles
        will be placed over this."""

        "Exception handling to handle which player is playing"
        "In this case if it is white's turn."
        p.draw.rect(screen, (p.Color("gold")), highlightP1)
        "Highlight that will show which player't turn it is."
    else:
        p.draw.rect(screen, (p.Color("gold")), highlightP2)
        "Highlight that will show which player't turn it is."

    if not gs.white_to_move:
        p.draw.rect(screen, (p.Color("black")), highlightP1)
        "Highlight that will show which player't turn it is."
    else:
        p.draw.rect(screen, (p.Color("black")), highlightP2)
        "Highlight that will show which player't turn it is."

    p.draw.rect(screen, (p.Color("darkcyan")), box1)
    p.draw.rect(screen, (p.Color("grey")), box2)
    screen.blit(player1, ((528, 105)))
    screen.blit(player2, ((530, 305)))
    screen.blit(white, ((590, 130)))
    screen.blit(black, ((590, 330)))
    "Drawing the squares"


def drawEndGameText(screen, text):
    "Part of the code that will print the last part of the game i.e. checkmate/stalemate"
    font = p.font.SysFont("Helvetica", 25, True, False)
    "font objects such as the colour and font style"
    text_object = font.render(text, False, p.Color("gray"))
    text_location = p.Rect(0, 0, width, height).move(width / 2 - text_object.get_width() / 2,
                                                     height / 2 - text_object.get_height() / 2)
    "location of the font saved in text_location"
    screen.blit(text_object, text_location)
    "produces the text_object on the screen"
    text_object = font.render(text, False, p.Color('black'))
    "location of the text_object saved in text_object"
    screen.blit(text_object, text_location.move(2, 2))
    "produces the text location on the board"

# Part of the code that will animate the chess moves.
def animateMove(move, screen, board, clock):
    "Part of the code that will animate the chess moves."
    global colors
    """Imports colors which is a library which contains colours, instead of
     entering RGB values, only entering string values is enough."""
    rows = move.end_row - move.start_row
    "subtracts the two variables to check the distance of animation"
    columns = move.end_col - move.start_col
    "subtracts the two variables to check the distance of animation"
    FPSpieceMove = 12  # frames to move one square
    "frames to move one square"
    FPScount = (abs(rows) + abs(columns)) * FPSpieceMove
    ""
    for frame in range(FPScount + 1):
        row, col = (move.start_row + rows * frame / FPScount, move.start_col + columns * frame / FPScount)
        drawBoard(screen)
        drawPieces(screen, board)
        # erase the piece moved from its ending square
        color = colors[(move.end_row + move.end_col) % 2]
        end_square = p.Rect(move.end_col * BOX_SIZE, move.end_row * BOX_SIZE, BOX_SIZE, BOX_SIZE)
        p.draw.rect(screen, color, end_square)
        # draw captured piece onto rectangle
        if move.piece_captured != '--':
            if move.is_enpassant_move:
                enpassant_row = move.end_row + 1 if move.piece_captured[0] == 'b' else move.end_row - 1
                end_square = p.Rect(move.end_col * BOX_SIZE, enpassant_row * BOX_SIZE, BOX_SIZE, BOX_SIZE)
            screen.blit(rendered[move.piece_captured], end_square)
        # draw moving piece
        screen.blit(rendered[move.piece_moved], p.Rect(col * BOX_SIZE, row * BOX_SIZE, BOX_SIZE, BOX_SIZE))
        p.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    playGame()

