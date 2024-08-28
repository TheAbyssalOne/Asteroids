import pygame
from constants import *
from circleshape import *
from player import *
from asteroid import *
from asteroidfield import *
from sys import exit



def main():
    print("Starting asteroids!")
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    
    # Set containers before instantiation
    Player.containers = (updatable, drawable)
    Asteroid.containers = (updatable, drawable, asteroids)
    AsteroidField.containers = (updatable,)  # Note the tuple format
    
    # Instantiate objects after setting containers
    player = Player(x=SCREEN_WIDTH / 2, y=SCREEN_HEIGHT / 2)
    new_asteroid_field = AsteroidField() 

    running = True
    while running:
        dt = clock.tick(60) / 1000
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill((0, 0, 0))  # Clear screen
        for x in updatable:
            x.update(dt)  # Update all updatable objects
        for x in asteroids:
            if CircleShape.check_collision(player, x):
                print("Game Over!")
                exit(0)
        for x in drawable:
            x.draw(screen)  # Draw all drawable objects
        pygame.display.flip()  # Update the entire display

    pygame.quit()

if __name__ == "__main__":
    main()

