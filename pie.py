import pygame
import math
import random


# FRAME CONSTRUCTION
def init_display():
	WIN = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
	WIDTH = 9 * pygame.display.Info().current_w // 10
	HEIGHT = 9 * pygame.display.Info().current_h // 10
	pygame.quit()
	WIN = pygame.display.set_mode((WIDTH, HEIGHT))
	pygame.display.set_caption('Golden Ratio')

	return WIN, WIDTH, HEIGHT


# INIT FRAME
WIN, WIDTH, HEIGHT = init_display()

# INIT @params
xc = WIDTH // 2
yc = HEIGHT // 2
rad = 200



# INIT Colours
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
ORANGE = (255, 165, 0)
TURQUOISE = (64, 224, 208)
PURPLE = (128, 0, 128)
YELLOW = (102, 102, 0)
MAGENTA = (102, 102, 105)

Color = [RED, GREEN, BLUE, WHITE, ORANGE, TURQUOISE, PURPLE, YELLOW, MAGENTA]



def golden():
    theta = 0
    
    while True:
        x0 = rad * math.cos(theta) + xc
        y0 = rad * math.sin(theta) + yc
        #pygame.draw.line(WIN, (0, 0, 255), (xc, yc), (x0, y0))

        x1 = rad * math.cos(math.pi * theta) + x0
        y1 = rad * math.sin(math.pi * theta) + y0
        #pygame.draw.line(WIN, (0, 0, 255), (x0, y0), (x1, y1))
        pygame.draw.circle(WIN, (0, 0, 255), (x1, y1), 1)
        pygame.display.flip()
        
        #pygame.draw.line(WIN, (0, 0, 0), (x0, y0), (x1, y1))
        #pygame.draw.line(WIN, (0, 0, 0), (xc, yc), (x0, y0))
        
        theta -= math.pi/720

         

def main():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                   golden()
	


if __name__ == '__main__':
	main()