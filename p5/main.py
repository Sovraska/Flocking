from boid import Boid
import py5

flocks = []


def setup():
    py5.size(640, 360)
    py5.frame_rate(60)
    py5.rect_mode(py5.CENTER)
    for i in range(40):
        flocks.append(Boid())


def draw():
    py5.background(51)
    for boid in flocks:
        boid.edges()
        boid.flock(flocks)
        boid.update()
        boid.show()


py5.run_sketch()
