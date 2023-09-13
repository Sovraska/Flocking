import pygame
from pygame import Rect

from setup import HEIGHT, screen, BLACK, GREEN, WIDTH, my_font, GREY

slider_pos = 0
slider_value = 0
slider_start_value = int(WIDTH / 3) / 2


class Slider:

    def __init__(self, name, slider_start_value, slider_h, slider_w, slider_start, slide_button_h, slide_button_w):
        self.name = name
        self.slider_pos = slider_start_value
        self.slider_h = slider_h
        self.slider_w = slider_w
        self.slider_start = slider_start
        self.slide_button_h = slide_button_h
        self.slide_button_w = slide_button_w
        self.slide_end = self.slider_start + self.slider_w

    def edges(self):
        mouse_pos = pygame.mouse.get_pos()[0] - 5
        if pygame.mouse.get_pressed()[0] != 0:
            if not self.slider_start < mouse_pos < self.slide_end:
                return
            else:
                self.slider_pos = mouse_pos
                self.slider_pos -= self.slider_start
                if self.slider_pos < 0:
                    self.slider_pos = 0
                if self.slider_pos > self.slider_w:
                    self.slider_pos = self.slider_w

    def show(self):
        slider_h = HEIGHT - self.slider_h
        pygame.draw.rect(screen, GREY, Rect(self.slider_start, slider_h, WIDTH, HEIGHT))

        pygame.draw.rect(screen, BLACK, Rect(self.slider_start, slider_h, 5, 40))
        pygame.draw.ellipse(screen, GREEN,
                         Rect(self.slider_pos + self.slider_start, slider_h, self.slide_button_w, self.slide_button_h), 20)
        posent = (self.slider_pos + 1) / self.slider_w
        text_surface = my_font.render(f"{round(posent * 100)} %", False, BLACK)
        screen.blit(text_surface, (self.slider_start + 5, slider_h))
