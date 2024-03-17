import pygame

# Инициализация Pygame
pygame.init()

# Установка размеров экрана
screen = pygame.display.set_mode((400, 300))
pygame.display.set_caption("Clicker Game")

# Цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Шрифт и начальное количество
font = pygame.font.Font(None, 36)
counter = 0

# Цикл игры
running = True
while running:
    screen.fill(WHITE)

    # Обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                counter += 10

    # Отображение количества на экране
    text = font.render(f"Count: {counter}", True, BLACK)
    text_rect = text.get_rect(center=(200, 150))
    screen.blit(text, text_rect)

    # Обновление экрана
    pygame.display.flip()

# Завершение Pygame
pygame.quit()