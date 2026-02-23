import pygame
from constants import *
from logger import log_state


def main():
    print("Starting Asteroids with pygame version: 2.6.1")
    print(f'''
Screen width: {SCREEN_WIDTH}
Screen height: {SCREEN_HEIGHT}
          ''')
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    log_state()
    while True:
        for event in pygame.event.get():
            pass
        screen.fill("black")
        pygame.display.flip()

#Do not modify below this line

if __name__ == "__main__":
    main()
