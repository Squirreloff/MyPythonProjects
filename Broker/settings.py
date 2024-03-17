from pygame import *
init()

W, H = 277, 600
sc = display.set_mode((W, H))
font = font.Font(None, 36) #ЗАГРУЗИТЬ СВОЙ FONT ИЗ FIGMA
click = 10000

circle1 = Rect(70, 530, 38, 38)
circle2 = Rect(120, 530, 38, 38)
circle3 = Rect(170, 530, 38, 38)
menu_val = 2
bt_menu = 2
x, y = 0, 0

#MENU 1
bt_kripta = Rect(0, 10, 275, 80)
bt_stocks = Rect(0, 100, 275, 80)
bt_portfolio = Rect(0, 190, 275, 80)

#MENU 2
button_rect = Rect(0, 100, 277, 400)

#MENU 3
bt_property = Rect(0, 10, 275, 80)
bt_transport = Rect(0, 100, 275, 80)
bt_art = Rect(0, 190, 275, 80)
bt_pet = Rect(0, 280, 275, 80)
