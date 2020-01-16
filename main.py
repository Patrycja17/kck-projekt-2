import pygame
import random
import time

pygame.init()
pygame.mixer.music.load("resources/light.wav")

display_width = 1280
display_height = 768
char_height = display_height * 0.45
char_width = display_width * 0.10
game_display = pygame.display.set_mode((display_width, display_height))

white = (255, 255, 255)
black = (0, 0, 0)
green = (0, 255, 0)
char = pygame.image.load('resources/char1.png').convert_alpha()
background = pygame.image.load('resources/8bitcitysynth.jpg').convert_alpha()
clock = pygame.time.Clock()
pygame.display.set_caption("Untitled Game", "Untitled Game")


def character(x, y):
    game_display.blit(char, (x, y))


def obstacles(objx, objy, objw, objh, color):
    pygame.draw.rect(game_display, color, [objx, objy, objw, objh])

def text_objects(text, font):
    textSurface = font.render(text, True, white)
    return textSurface, textSurface.get_rect()


def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf', 115)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_width / 2), (display_height / 4))
    game_display.blit(TextSurf, TextRect)


def game_loop():
    pygame.mixer.music.set_volume(0.03)
    pygame.mixer.music.play(-1)
    obstacle_start_x = 1300
    obstacle_speed = 10
    obstacle_start_y = (display_height * 0.45) + 140
    random_width = random.randint(50, 1000)

    char_x = display_width * 0.1
    char_y = display_height * 0.45
    game_exit = False
    while not game_exit:
        # obsługa zdarzeń
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_exit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if char_y == display_height * 0.45:
                        char_y += 120
                    else:
                        char_y -= 120
                if event.key == pygame.K_ESCAPE:
                    game_exit = True
        # wyświetlanie tła
        game_display.blit(background, (0, 0))
        message_display("Spacebar to move")
        character(char_x, char_y)
        obstacles(obstacle_start_x, obstacle_start_y, random_width, 134, green)
        if obstacle_start_x + random_width <= 0:
            obstacle_start_x = 1300
            random_width = random.randint(50, 1000)
            if char_y == display_height * 0.45:
                obstacle_start_y = char_y + 134
            else:
                obstacle_start_y = char_y - 134

        obstacle_start_x -= obstacle_speed
        pygame.display.flip()
        clock.tick(60)


game_loop()
pygame.quit()
quit()
