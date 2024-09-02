import pygame
from constants import *
from circleshape import *
from player import *
from asteroid import *
from asteroidfield import *
from shot import *
from sys import exit

# Extending the project

# You've done all the required steps, but if you'd like to make the project your own, here are some ideas:

#     Add a scoring system
#     Implement multiple lives and respawning
#     Add an explosion effect for the asteroids
#     Add acceleration to the player movement
#     Make the objects wrap around the screen instead of disappearing
#     Add a background image
#     Create different weapon types
#     Make the asteroids lumpy instead of perfectly round
#     Make the ship have a triangular hit box instead of a circular one
#     Add a shield power-up
#     Add a speed power-up
#     Add bombs that can be dropped


def main():
    print("Starting asteroids!")
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    
    # Set containers before instantiation
    Player.containers = (updatable, drawable)
    Asteroid.containers = (updatable, drawable, asteroids)
    AsteroidField.containers = (updatable,)  # Note the tuple format
    Shot.containers = (updatable,drawable, shots) 
    
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
        for shot in shots:
            for asteroid in asteroids:
                if CircleShape.check_collision(shot, asteroid):
                    shot.kill()
                    asteroid.split()
        for x in drawable:
            x.draw(screen)  # Draw all drawable objects
        pygame.display.flip()  # Update the entire display
 
    pygame.quit()

if __name__ == "__main__":
    main()