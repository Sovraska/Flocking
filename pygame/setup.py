import pygame

WIDTH = 640 * 2
HEIGHT = 380 * 2
FPS = 30

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREY = (51, 51, 51)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
screen = pygame.display.set_mode((WIDTH, HEIGHT))
# создаем игру и окно
pygame.init()
pygame.mixer.init()  # для звука

pygame.display.set_caption("My Game")
clock = pygame.time.Clock()
pygame.init()

pygame.font.init()
my_font = pygame.font.SysFont('Comic Sans MS', 30)

flocks = []



