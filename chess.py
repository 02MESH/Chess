import pygame as p
from pygame.locals import *
import sys as s
"Importing vital pane production libraries"
import webbrowser as browse
"""Importing webbrowser to open the url if the user does not
know to play chess."""
from modes.multiplayer import multiplayerENGINE
from modes.singleplayer import singleplayerENGINE
"Importing the chess engine."

background = p.image.load('resources/' + 'background.jpg' )
icon = p.image.load('resources/' + 'icon.gif')
p.init()
clock = p.time.Clock()
p.display.set_caption("CHESS")
"Setting the main pane window name as CHESS"
p.display.set_icon(icon)
"Setting the pane window as a chess icon"

font = p.font.SysFont("Helvetica", 30)
smallFont = p.font.SysFont("Aleo", 25)
main_font = p.font.SysFont("Aleo", 90)
incomplete_font = p.font.SysFont("Aleo", 50)
"Setting font variables to produce text."

screen = p.display.set_mode((500,500), 0, 32)
"Declaring screen to be accessed by the program"

darkCyan = (23,174,165)
black = (0,0,0)
white = (255,255,255)
"Setting colour RGB variables."

def text_generator(text, font, colour, surface, x, y):
    "Subroutine that will generate the MAIN MENU text on screen"
    textObject = font.render(text, 1, colour)
    textrectangle = textObject.get_rect()
    textrectangle.topleft = (x, y)
    surface.blit(textObject, textrectangle)


valid = True
"Flag variable that will run the main loop"

def mainGUI():
    "Subroutine that will manage the full game"
    clicked = False
    "Flag variable that will check if the user clicked"

    while valid:
        "Infinite loop that will run the game."

        screen.fill((255,255,255))
        screen.blit(background, (0, 0))
        mainMenu = p.Rect((70,12), (360,50))
        p.draw.rect(screen, (black), mainMenu)
        text_generator("MAIN MENU", main_font, (255,255,255), screen, 70,10)
        "Producing the main pane."

        mouseX, mouseY = p.mouse.get_pos()
        "Variable that will get the x and y positions of the mouse."

        but1TEXT = font.render("SINGLE PLAYER", True, white)
        but2TEXT = font.render("MULTIPLAYER", True, white)
        but3TEXT = font.render("ONLINE", True, white)
        but4TEXT = font.render("EXIT", True, white)
        howToTEXT = smallFont.render("HOW TO PLAY CHESS", True, white)
        basicCommands = smallFont.render("SHORTCUT COMMANDS", True, white)
        "Variables that will save the button text."

        but1 = p.Rect((150,100), (200,50))
        but2 = p.Rect((150,200), (200,50))
        but3 = p.Rect((150,300), (200,50))
        but4 = p.Rect((150,400), (200,50))
        howTobut = p.Rect((0,460), (180,50))
        commands = p.Rect((285,460), (210,50))
        "Variables that will save the button rectangles with their positions."

        if but1.collidepoint((mouseX, mouseY)):
            "If button 1 is clicked"
            if clicked:
                singleplayer()
        if but2.collidepoint((mouseX, mouseY)):
            "If button 2 is clicked"
            if clicked:
                multiplayer()
        if but3.collidepoint((mouseX, mouseY)):
            "If button 3 is clicked"
            if clicked:
                online()
        if but4.collidepoint((mouseX, mouseY)):
            "If button 4 is clicked"
            if clicked:
                p.quit()
        if howTobut.collidepoint((mouseX, mouseY)):
            "If the howTobutton is clicked."
            if clicked:
                howTo()
        if commands.collidepoint((mouseX, mouseY)):
            "If the commands button is clicked."
            if clicked:
                shortcut()

        p.draw.rect(screen, (black), but1)
        p.draw.rect(screen, (black), but2)
        p.draw.rect(screen, (black), but3)
        p.draw.rect(screen, (black), but4)
        p.draw.rect(screen, (black), howTobut)
        p.draw.rect(screen, (black), commands)
        "Program lines that will produce the rectangle buttons."

        screen.blit(but1TEXT, (155, 105))
        screen.blit(but2TEXT, (170, 205))
        screen.blit(but3TEXT, (200, 305))
        screen.blit(but4TEXT, (220, 405))
        screen.blit(howToTEXT, (0,470))
        screen.blit(basicCommands, (290, 470))
        "Program lines that will produce the text on the buttons."

        clicked = False
        for event in p.event.get():
            "Loop that will manage user inputs."
            if event.type == QUIT:
                "If the user clicks the close button on the pane."
                p.quit()
                s.exit()
                "Ending the game"
            if event.type == KEYDOWN:
                "If the user clicks a keyboard button"
                if event.key == K_ESCAPE:
                    p.quit()
                    s.exit()
                    "Ending the game."
            if event.type == MOUSEBUTTONDOWN:
                "If the user clicks a mouse button"
                if event.button == 1:
                    "If the user clicks the mouse button once."
                    clicked = True
                    "Mouse clicked will be true."

        p.display.update()
        clock.tick(60)


def singleplayer():
    "Subroutine that calls the singleplayer subroutine"
    singleplayerENGINE.playGame()

def multiplayer():
    "Subroutine that calls the multiplayer subroutine"
    multiplayerENGINE.playGame()

def howTo():
    "Subroutine that will open the how to play chess link."
    browse.open_new("https://www.chess.com/learn-how-to-play-chess")

####ONLINE#####

def online():
    "Subroutine that will manage the play online game mode."

    BUT1ONLINE = p.Rect((150, 100), (200, 50))
    BUT2ONLINE = p.Rect((150, 200), (200, 50))
    BUT3ONLINE = p.Rect((150, 300), (200, 50))
    "Variables that holds the button positions"

    host = font.render("HOST GAME", True, white)
    join = font.render("JOIN GAME", True, white)
    joinchatroom = font.render("CHAT", True, white)
    "Subroutine that will hold the text data to position on the buttons."

    run = True
    "Flag variable that will manage the loop"
    click = False
    "Flag variable that will manage the mouse clicks"
    while run:
        screen.fill((255, 255, 255))
        screen.blit(background, (0, 0))
        mouseXpos, mouseYpos = p.mouse.get_pos()
        "Code similar to the mainGUI() subroutine"

        if BUT1ONLINE.collidepoint((mouseXpos, mouseYpos)):
            "If the user clicks the first button from online mode"
            if click:
                incomplete()
        if BUT2ONLINE.collidepoint((mouseXpos, mouseYpos)):
            "If the user clicks the second button from online mode"
            if click:
                incomplete()
        if BUT3ONLINE.collidepoint((mouseXpos, mouseYpos)):
            "If the user clicks the third button from online mode"
            if click:
                didnotINTEGRATE()

        p.draw.rect(screen, (black), BUT1ONLINE)
        p.draw.rect(screen, (black), BUT2ONLINE)
        p.draw.rect(screen, (black), BUT3ONLINE)
        "Drawing the buttons"

        screen.blit(host, (175, 105))
        screen.blit(join, (175, 205))
        screen.blit(joinchatroom, (200, 305))
        "Drawing the text on the buttons"

        click = False

        for event in p.event.get():
            "Managing the user inputs"
            if event.type == QUIT:
                "If the user clicks the close button on the pane"
                p.quit()
                s.exit()
            if event.type == KEYDOWN:
                "If the user enter a keyboard key"
                if event.key == K_ESCAPE:
                    run = False
            if event.type == MOUSEBUTTONDOWN:
                "If the user enters a mouse button"
                if event.button == 1:
                    click = True

        p.display.update()
        clock.tick(60)

def incomplete():
    "Subroutine that will display that the online mode is not complete"
    running = True
    messageLINE1 = "This part of the"
    messageLINE2 = "game has not been"
    messageLINE3 = "completed yet :("

    printMESSAGE1 = incomplete_font.render(messageLINE1, True, white)
    printMESSAGE2 = incomplete_font.render(messageLINE2, True, white)
    printMESSAGE3 = incomplete_font.render(messageLINE3, True, white)
    textBACKGROUND = p.Rect((50, 50), (400, 400))

    while running:
        screen.fill((0,0,0))
        screen.blit(background, (0, 0))
        p.draw.rect(screen, (black), textBACKGROUND)

        screen.blit(printMESSAGE1, (120, 100))
        screen.blit(printMESSAGE2, (100, 200))
        screen.blit(printMESSAGE3, (110, 300))

        for event in p.event.get():
            if event.type == QUIT:
                p.quit()
                s.exit
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False

        p.display.update()
        clock.tick(60)

def didnotINTEGRATE():
    """Subroutine that will display that the chat app is not
    integrated with the mainGUI."""
    running = True
    messageLINE1 = "This part of the"
    messageLINE2 = "game has been"
    messageLINE3 = "finished but not"
    messageLINE4 = "been integrated with"
    messageLINE5 = "the chess.py file."

    printMESSAGE1 = incomplete_font.render(messageLINE1, True, white)
    printMESSAGE2 = incomplete_font.render(messageLINE2, True, white)
    printMESSAGE3 = incomplete_font.render(messageLINE3, True, white)
    printMESSAGE4 = incomplete_font.render(messageLINE4, True, white)
    printMESSAGE5 = incomplete_font.render(messageLINE5, True, white)
    textBACKGROUND = p.Rect((50, 50), (400, 300))

    while running:
        screen.fill((0,0,0))
        screen.blit(background, (0, 0))
        p.draw.rect(screen, (black), textBACKGROUND)

        screen.blit(printMESSAGE1, (120, 60))
        screen.blit(printMESSAGE2, (120, 110))
        screen.blit(printMESSAGE3, (110, 160))
        screen.blit(printMESSAGE4, (90, 210))
        screen.blit(printMESSAGE5, (110, 260))

        for event in p.event.get():
            if event.type == QUIT:
                p.quit()
                s.exit
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False

        p.display.update()
        clock.tick(60)
#####END OF ONLINE########


def shortcut():
    """Subroutine that will display to the user the different
    shortcuts the user can use."""
    running = True
    pressESC = "• Press esc to go back"
    pressESC2 = "to the main menu."
    pressZ = "• Press Z to rewind in"
    pressZ2 = "games."
    pressR = "• Press R to reset the"
    pressR2 = "board."


    printMESSAGE1 = incomplete_font.render(pressESC, True, white)
    printMESSAGE2 = incomplete_font.render(pressESC2, True, white)
    printMESSAGE3 = incomplete_font.render(pressZ, True, white)
    printMESSAGE4 = incomplete_font.render(pressZ2, True, white)
    printMESSAGE5 = incomplete_font.render(pressR, True, white)
    printMESSAGE6 = incomplete_font.render(pressR2, True, white)


    textBACKGROUND = p.Rect((50, 50), (400, 250))

    while running:
        screen.fill((0,0,0))
        screen.blit(background, (0, 0))
        p.draw.rect(screen, (black), textBACKGROUND)

        screen.blit(printMESSAGE1, (75, 60))
        screen.blit(printMESSAGE2, (95, 90))
        screen.blit(printMESSAGE3, (75, 140))
        screen.blit(printMESSAGE4, (95, 170))
        screen.blit(printMESSAGE5, (75, 220))
        screen.blit(printMESSAGE6, (95, 250))

        for event in p.event.get():
            if event.type == QUIT:
                p.quit()
                s.exit
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False

        p.display.update()
        "Updates the screen."
        clock.tick(60)
        "Refreshing the screen 60 times a second"

if __name__ == "__main__":
    "Calls the main subroutine."
    mainGUI()