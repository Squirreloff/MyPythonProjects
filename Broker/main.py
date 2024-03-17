from pygame import *
from Board import *
from settings import *
init()
board = Board(sc)

run = True
while run:
    mx, my = mouse.get_pos()
    for e in event.get():
        if e.type == QUIT:
            run = False
        elif e.type == MOUSEBUTTONDOWN:
            if e.button == 1:
                if circle1.collidepoint(e.pos):
                    menu_val = 1
                elif circle2.collidepoint(e.pos):
                    menu_val = 2
                elif circle3.collidepoint(e.pos):
                    menu_val = 3
                if bt_menu == 2:
                    if button_rect.collidepoint(e.pos):
                        click += 10
                elif bt_menu == 3:
                    if bt_property.collidepoint(e.pos):
                        menu_val = 4
                    elif bt_transport.collidepoint(e.pos):
                        print(2)
                    elif bt_art.collidepoint(e.pos):
                        print(3)
                    elif bt_pet.collidepoint(e.pos):
                        print(4)
                elif bt_menu == 1:
                    if bt_kripta.collidepoint(e.pos):
                        print(1)
                    elif bt_stocks.collidepoint(e.pos):
                        print(2)

    if menu_val == 2:
        board.draw(2, 0, 0)
        bt_menu = 2
    elif menu_val == 3:
        board.draw(3, 0, 0)
        bt_menu = 3
    elif menu_val == 1:
        board.draw(1, 0, 0)
        bt_menu = 1
    elif menu_val == 4:
        board.draw(4, 0, 0)

        # БД
        """
        Вопросы
        1. Как сделать удаление кнопок при нажатии кнопки на bt_menu 3
        2. Как скроллить экран
        
        """
