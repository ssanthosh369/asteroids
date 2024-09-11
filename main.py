import sys
from asteroidfield import AsteroidField
import pygame 
from constants import *
from player import Player
from asteroid import Asteroid
from shot import Shot

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock() 
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (updatable, drawable, asteroids)
    AsteroidField.containers = updatable
    Shot.containers = (shots, updatable, drawable)

    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    player = Player(x, y)
    asteroidfield =  AsteroidField()

    while(True): 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        screen.fill(color = "black")

        for asteroid in asteroids:
            if player.check_collision(asteroid):
                print("Game over!")
                sys.exit()

            for shot in shots:
                if asteroid.check_collision(shot):
                    asteroid.split()
                    shot.kill()


        for i in updatable:
            i.update(dt)
            
        for i in drawable:
            i.draw(screen)

        pygame.display.flip()

        dt = clock.tick(60)/1000
        

if __name__ == "__main__":
    main()