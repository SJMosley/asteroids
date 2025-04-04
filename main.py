import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from player import Player
# from constants import ASTEROID_MIN_RADIUS, ASTEROID_MAX_RADIUS, ASTEROID_KINDS, ASTEROID_SPAWN_RATE

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)

    while True:
        #allow for quirting
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        #Start - Screen Prep
        screen.fill("black")
        #End - Screen Prep

        player.draw(screen)

        #Start - End of loop iteration
        dt = clock.tick(60)/1000
        pygame.display.flip()
        #End - End of loop iteration
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

if __name__ == "__main__":
    main()
