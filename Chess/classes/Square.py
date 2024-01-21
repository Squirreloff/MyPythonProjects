from pygame import *


class Square:

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.pos = (x, y)
        self.abs_x = x * width # ШИРИНА И ВЫСОТА ПОЛЯ В ПИКСИЛЯХ
        self.abs_y = y * height
        self.abs_pos = (x * width, y * height)
        self.color = 'light' if (x + y) % 2 == 0 else 'dark'
        self.draw_color = (220, 208, 194) if self.color == 'light' else (53, 53, 53)
        self.highlight_color = (100, 249, 83) if self.color == 'light' else (0, 228, 10)
        self.occupying_piece = None    #КАКАЯ ФИГУРА В КЛЕТКЕ
        self.coord = self.get_coord()
        self.highlight = False #ВЫДЕЛИНА ЛИ КЛЕТКА
        self.rect = Rect(
            self.abs_x,
            self.abs_y,
            self.width,
            self.height
        )

    def get_coord(self):
        columns = 'abcdefgh'
        return columns[self.x] + str(self.y + 1)

    def draw(self, sc):
        if self.highlight:
            draw.rect(sc, self.highlight_color, self.rect)
        else:
            draw.rect(sc, self.draw_color, self.rect)
        if self.occupying_piece is not None:
            centering_rect = self.occupying_piece.img.get_rect()
            centering_rect.center = self.rect.center
            sc.blit(self.occupying_piece.img, centering_rect.topleft)
