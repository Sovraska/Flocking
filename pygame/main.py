import pygame


from setup import clock, FPS, screen, GREY, flocks, WIDTH
from slider import Slider, slider_start_value


def set_up_slider():
    print(int(WIDTH / 3))
    slider_align = Slider("align", slider_start_value, 40, int(WIDTH / 3), 5, 40, 10)
    slider_cohesion = Slider("cohesion", slider_start_value, 40, int(WIDTH / 3), int(WIDTH / 3), 40, 10)
    slider_separation = Slider("separation", slider_start_value, 40, int(WIDTH / 3), int(WIDTH / 3) * 2, 40, 10)
    return [slider_align, slider_cohesion, slider_separation]


if __name__ == '__main__':
    from boid import Boid
    for i in range(100):
        flocks.append(Boid())
    slider_align, slider_cohesion, slider_separation = set_up_slider()
    running = True

    while running:

        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        pygame.display.update()
        screen.fill(GREY)
        for boid in flocks:
            boid.edges()
            boid.flock(flocks, slider_align.slider_pos, slider_cohesion.slider_pos, slider_separation.slider_pos)
            boid.update()
            boid.show()

        slider_align.edges()
        slider_align.show()

        slider_cohesion.edges()
        slider_cohesion.show()

        slider_separation.edges()
        slider_separation.show()


        pygame.display.flip()
    pygame.quit()
