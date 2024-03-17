from pygame import *
from settings import *

init()


class Board:
    def __init__(self, sc):
        self.sc = sc

    def draw(self, num, x, y):
        sc.fill('white')
        if num == 2:
            img = image.load('Menu.png')
            sc.blit(img, (0, 0))
            text = font.render(f'{click}', True, 'black')
            text_rect = text.get_rect(center=(150, 150))
            sc.blit(text, text_rect)
        elif num == 3:
            img = image.load('Own.png')
            sc.blit(img, (0, 0))
        elif num == 1:
            img = image.load('birsha.png')
            sc.blit(img, (0, 0))
        elif num == 4:
            img = image.load('Property.png')
            img.scroll(x, y)
            sc.blit(img, (x, y))
        display.update()
