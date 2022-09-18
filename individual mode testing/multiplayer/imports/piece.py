import pygame as p
import resources

BOX_SIZE = 500//8
"The size of the single box will be achieved by dividing the HEIGHT/WIDTH by dimension i.e. 100"
rendered = {}
"Dictionary where the rendered images will be saved at"

def RenderImage():
    pieces = ['wp', 'wR', 'wN', 'wB', 'wK', 'wQ', 'bp', 'bR', 'bN', 'bB', 'bK', 'bQ']
    "Piece saved in the form of strings."
    for piece in pieces:
        rendered[piece] = p.transform.scale(p.image.load("resources/" + piece + ".png"), (BOX_SIZE, BOX_SIZE))
        """The for loop will go through the pictures in the resources library which fetch and
        render the image i.e. p.transform.scale which are the images specified by the BOX_SIZE."""

