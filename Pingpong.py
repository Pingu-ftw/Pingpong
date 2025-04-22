from pygame import *
win_width = 800
win_height = 500
window = display.set_mode((win_width, win_height))
lightblue = (173,216,230)
window.fill(lightblue)
clock = time.Clock()
FPS = 60
game = True
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    display.update()
    clock.tick(FPS)