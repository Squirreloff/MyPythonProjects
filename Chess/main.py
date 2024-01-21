from pygame import *
from classes.Board import Board
init()

WINDOW_SIZE = (600, 600)
sc = display.set_mode(WINDOW_SIZE)

board = Board(WINDOW_SIZE[0], WINDOW_SIZE[1])

def draw(screen):
    screen.fill('white')
    board.draw(screen)
    display.update()

if __name__ == '__main__':
    run = True
    while run:
        mx, my = mouse.get_pos()
        for e in event.get():
            if e.type == QUIT:
                run = False
            if e.type == MOUSEBUTTONDOWN:
                if e.button == 1:
                    board.handle_click(mx, my)
        if board.is_in_checkmate('white'):
            print('Black wins')
            run = False
        elif board.is_in_checkmate('black'):
            print('White wins')
            run = False
        draw(sc)
