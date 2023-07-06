import pygame
import math


def formel(xk):
    return math.cos(math.asin(xk))


if __name__ == '__main__':
    D = []
    lol = 500
    lines = 500
    pygame.init()
    screen_width = 1000
    screen_height = 1000
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption('circle test')
    screen.fill('white')
    for Xline in range(0, 1000):
        y = formel(xk=Xline / 500 - 1)
        screen.set_at((Xline, int(500 + (y * 500))), 'black')
        screen.set_at((Xline, int(500 + (-y * 500))), 'black')
        collecter = int(500 + (y * 500))
        D.append(collecter)
    for index in range(0, lines):
        pygame.draw.line(surface=screen, color='blue', start_pos=(index, D[index]), end_pos=(index + lol, D[index + lol]), width=1)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        pygame.display.flip()
