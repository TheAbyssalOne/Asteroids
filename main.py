import pygame
from constants import *
from player import *



def main():
    print("Starting asteroids!")
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    player = Player(x=SCREEN_WIDTH / 2, y=SCREEN_HEIGHT / 2)
    running = True
    
    while running:
        dt = clock.tick(60) / 1000
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill((0, 0, 0))  # Clear screen
        for x in updatable:
            x.update(dt) # Update player position and state
        for x in drawable:
            x.draw(screen) # Draw player
        pygame.display.flip()  # Update entire display

    pygame.quit()

if __name__ == "__main__":
    main()
