import pygame
import sys
import time

if __name__ == '__main__':
    land = "burlywood4"
    water = "blue"
    line_color = "black"
    player_color = "grey"
    screen_coler = "white"
    pygame.init()
    clock = pygame.time.Clock()
    window_w = 1000
    window_l = 1000
    game_on = 1
    screen = pygame.display.set_mode((window_w, window_l))
    pygame.display.set_caption('snake game')
    player = pygame.Rect(window_w / 2 + 10, window_l / 2 + 10, 100 - 10, 100 - 10)
    player_speed_x = 0
    player_speed_y = 0
    while True:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
                if player_speed_x == 0:
                    player_speed_x = 10
                    player_speed_y = 0
                else:
                    player_speed_x *= -1

            if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
                if player_speed_x == 0:
                    player_speed_x = 10
                    player_speed_y = 0
                else:
                    player_speed_x *= -1

            if event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
                if player_speed_y == 0:
                    player_speed_x = 0
                    player_speed_y = 10
                else:
                    player_speed_y *= -1

            if event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
                if player_speed_y == 0:
                    player_speed_x = 0
                    player_speed_y = 10
                else:
                    player_speed_y *= -1



        line_p_x = 0
        line_p_y = 0
        line_width_long = 10
        line_legth_long = 1000

        line_legth_tall = 10
        line_width_tall = 1000

        screen.fill(screen_coler)

        color_lu = pygame.Rect(0, 0, window_w / 2, window_l / 2)
        pygame.draw.rect(screen, land, color_lu)

        color_ld = pygame.Rect(0, window_l / 2, window_w / 2, window_l / 2)
        pygame.draw.rect(screen, water, color_ld)

        color_ru = pygame.Rect(window_w / 2, 0, 500, 500)
        pygame.draw.rect(screen, water, color_ru)

        color_rd = pygame.Rect(window_w / 2, window_l / 2, window_w / 2, window_l / 2)
        pygame.draw.rect(screen, land, color_rd)

        # brige_

        for wid in (0, 100, 200, 300, 400, 500, 600, 700, 800, 900, 1000):
            line_tall = pygame.Rect(line_p_x, line_p_y + wid, line_width_tall, line_legth_tall)
            pygame.draw.rect(screen, line_color, line_tall)

        for leg in (0, 100, 200, 300, 400, 500, 600, 700, 800, 900, 1000):
            line_long = pygame.Rect(line_p_x + leg, line_p_y, line_width_long, line_legth_long)
            pygame.draw.rect(screen, line_color, line_long)



        #player_speed = player_speed + 100 / 15
        player.x = player.x + player_speed_x
        player.y = player.y + player_speed_y
        pygame.draw.rect(screen, player_color, player)
        pygame.display.flip()
