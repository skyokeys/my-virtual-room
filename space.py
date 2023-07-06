import pygame
import sys

if __name__ == '__main__':
    import pygame

    aliens = 0
    click_bonus = 0

    pygame.init()
    alien_poX = 0
    alien_poY = 500 - 200  # højre hjøne pos
    alien_sizeY = 400
    alien_sizeX = 400
    cookies_displayXpos = 0
    cookies_displayYpos = 0
    screen_width, screen_height = 1000, 1000
    screen = pygame.display.set_mode((screen_height, screen_height))
    pygame.display.set_caption("space game")
    big_alien = pygame.image.load('pycharm resources/1000_F_295595675_eRRv0gCe2ECYd2BxmqW7gnZTYepgz0uT.jpg')
    screen.fill('white')
    image_size = (alien_sizeX, alien_sizeY)

    alien = pygame.transform.scale(big_alien, image_size)
    alien_rect = alien.get_rect()
    alien_rect.x = alien_poX
    alien_rect.y = alien_poY
    screen.blit(alien, alien_rect)
    font = pygame.font.SysFont('arial', 35)
    alien_display_text = f'Aliens = {aliens}'
    cookies_display = font.render(alien_display_text, True, 'black')
    screen.blit(cookies_display, (cookies_displayXpos, cookies_displayYpos))


    running = True
    while running:
        for event in pygame.event.get():
            cookies_display = font.render(alien_display_text, True, 'black')
            screen.blit(cookies_display, (cookies_displayXpos, cookies_displayYpos))
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if alien_rect.collidepoint(*pygame.mouse.get_pos()):
                    aliens = aliens + 1 + click_bonus
                    test_box = pygame.Rect(screen_width/2, screen_height/2, screen_width/2, screen_height/2)
                    pygame.draw.rect(surface=screen, color='red', rect=test_box)
        cookies_display = font.render(alien_display_text, True, 'black')
        screen.blit(cookies_display, (cookies_displayXpos, cookies_displayYpos))
        pygame.display.flip()
