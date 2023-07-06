# Baseret på https://github.com/clear-code-projects/Pong_in_Pygame

import sys
import random
import pygame
if __name__ == '__main__':
    pygame.init() #for pygame frem
    clock = pygame.time.Clock()
    screen_width = 1000
    screen_height = 1000
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption('Pong')

    ball = pygame.Rect(0, 0, 50, 50)
    ball.centerx = int(screen_width/2)
    ball.centery = int(screen_height/2)

    player = pygame.Rect(screen_width - 20, screen_height / 2 - 70, 10, 140)
    opponent = pygame.Rect(10, screen_height / 2 - 70, 10, 140)

    ball_speed_x = 20
    ball_speed_y = 10
    player_x_speed = 0
    player_y_speed = 0
    opponent_speed = 8

    while True:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                #op control
                if event.key == pygame.K_UP:
                    player_y_speed -= 8
                #ned control
                elif event.key == pygame.K_DOWN:
                    player_y_speed += 8

            elif event.type == pygame.KEYUP:
                #hold inde control
                if event.key == pygame.K_UP:
                    player_y_speed += 8
                #hold inde control
                elif event.key == pygame.K_DOWN:
                    player_y_speed -= 8

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    player_x_speed -= 8
                elif event.key == pygame.K_UP:
                    player_x_speed += 8

            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    player_x_speed -= 8
                elif event.key == pygame.K_UP:
                    player_x_speed += 8



        player.y += player_y_speed
        player.x += player_x_speed
        if player.top < 0:
            player.top = 0
        if player.bottom > screen_height:
            player.bottom = screen_height

        if opponent.top < ball.y:
            opponent.y += opponent_speed

        if opponent.bottom > ball.y:
            opponent.y -= opponent_speed

        if opponent.top < 0:
            opponent.top = 0

        if opponent.bottom > screen_height:
            opponent.bottom = screen_height

        ball.x += ball_speed_x
        ball.y += ball_speed_y
        if ball.top <= 0 or ball.bottom >= screen_height:
            ball_speed_y *= -1
        if ball.left <= 0 or ball.right >= screen_width:
            ball_speed_x *= -1
        if ball.colliderect(player) or ball.colliderect(opponent):
            ball_speed_x *= -1
        radius = 6
        diameter = 12
        screen.fill('blue')
        pygame.draw.rect(screen, 'grey', player)
        pygame.draw.rect(screen, 'grey', opponent)
        pygame.draw.rect(screen, 'grey', ball)
        pygame.draw.aaline(screen, 'grey', (screen_width / 2, 0), (screen_width / 2, screen_height))
        pygame.draw.aaline(screen, 'grey', (screen_width / 2, 0), (screen_width / 2, screen_height))
        pygame.display.flip()
        clock.tick(60)