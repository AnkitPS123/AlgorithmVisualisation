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
	pygame.display.set_caption('Fourier Transform')

	return WIN, WIDTH, HEIGHT


# INIT FRAME
WIN, WIDTH, HEIGHT = init_display()

# INIT @params
xc = 70
yc = 150
hc = 100
rxc = 600
ryc = 800
hrc = 200



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


#axes
pygame.draw.line(WIN, WHITE, (xc, yc-hc), (xc, yc+hc))
pygame.draw.line(WIN, WHITE, (0, yc), (WIDTH, yc))
pygame.draw.line(WIN, WHITE, (rxc-hrc, ryc), (rxc+hrc, ryc))
pygame.draw.line(WIN, WHITE, (rxc, ryc-hrc), (rxc, ryc+hrc))
pygame.display.update()


def draw_vector(x, y, id):
    pygame.draw.circle(WIN, Color[id], (x, y), 2)
    pygame.draw.line(WIN, Color[id], (rxc, ryc), (x, y))


def fourier(Data):
    Data.sort()
    x0 = rxc
    y0 = ryc
    f = 0.0005
    rgb = 0
    for x in range(0, 10):
        for i in range(len(Data)):
            pygame.time.Clock().tick(60)
            pygame.draw.line(WIN, BLACK, (Data[i-1][0], yc), (Data[i-1][0], Data[i-1][1]))
            pygame.draw.line(WIN, GREEN, (Data[i][0], yc), (Data[i][0], Data[i][1]))
            pygame.draw.line(WIN, BLACK, (rxc, ryc), (x0, y0))
            gx = Data[i][1] - yc
            x0 = gx * math.cos(2*math.pi*f*i) + rxc
            y0 = gx * math.sin(2*math.pi*f*i) + ryc
            draw_vector(x0, y0, rgb)
            pygame.display.update()
            f += 0.005
        rgb += 1
        rgb %= len(Color)



def sample_data(D):
    f = 0.005
    gx = 50
    for i in range(WIDTH):
        D.append((i, gx * math.sin(2*math.pi*i*f) + yc))
        pygame.draw.circle(WIN, BLUE, (D[i][0], D[i][1]), 2)
    pygame.display.update()

def main():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        
            elif pygame.mouse.get_pressed()[0]:
                Data.append(pygame.mouse.get_pos())
                pygame.draw.circle(WIN, BLUE, (Data[-1][0], Data[-1][1]), 2)
                pygame.display.update()
                
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    Data = []
                    sample_data(Data)
                    fourier(Data)
	


if __name__ == '__main__':
	main()