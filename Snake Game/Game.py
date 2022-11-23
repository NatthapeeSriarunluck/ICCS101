import pygame
from pygame.locals import *

class Game:
    def __init__(self):
        # initialize pygame
        pygame.init()
        pygame.display.set_caption('ICCS101 - SNAKE')

        # timing parameters
        self.clock = pygame.time.Clock()
        self.FPS = 30
        self.gameSpeed = 3 # update player every 3 frames

        # graphics
        self.maxX = 20
        self.maxY = 20
        self.blockSize = 40
        self.windowWidth = self.maxX * self.blockSize
        self.windowHeight = self.maxY * self.blockSize
        self.screen = pygame.display.set_mode(
            (self.windowWidth, self.windowHeight),
            pygame.HWSURFACE)
        self.bgImage = pygame.image.load("assets/bg.jpg").convert()


        self.reset()

    def reset(self):
        '''
        Reset the game
        '''
        pass

    def update(self):
        '''
        Update vairous game objects
        '''
        pass

    def run(self):
        '''
        Main game loop
        '''
        frame_count = 0
        # Loop forever
        while (True):
            pygame.event.pump()
            keys = pygame.key.get_pressed()

            if (keys[K_RIGHT]):
                print('RIGHT')

            if (keys[K_LEFT]):
                print('LEFT')

            if (keys[K_UP]):
                print('UP')

            if (keys[K_DOWN]):
                print('DOWN')

            # Exit the game
            if (keys[K_ESCAPE]):
                break

            # update the game
            if frame_count > self.gameSpeed:
                self.update()
                frame_count = 0

            frame_count += 1

            # limit game speed
            self.clock.tick(self.FPS)

        pygame.quit()