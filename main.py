import sys
import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
# from constants import ASTEROID_MIN_RADIUS, ASTEROID_MAX_RADIUS, ASTEROID_KINDS, ASTEROID_SPAWN_RATE

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()

    Asteroid.containers = (updatable, drawable, asteroids)
    AsteroidField.containers = (updatable)
    Player.containers = (updatable, drawable)

    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    asteroid_field = AsteroidField()
    dt = 0

    while True:
        #allow for quirting
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        #Start - Screen Prep
        updatable.update(dt)
        for asteroid in asteroids:
            if asteroid.collides_with(player): #as a question
                print("Game Over!")
                sys.exit()
        screen.fill("black")
        #End - Screen Prep

        for item in drawable:
            item.draw(screen)

        #Start - End of loop iteration
        pygame.display.flip()
        dt = clock.tick(60)/1000
        #End - End of loop iteration
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

if __name__ == "__main__":
    main()
