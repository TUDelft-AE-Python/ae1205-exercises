import pygame as pg

## INITIALISATION CODE BLOCK
pg.init()

reso = (750, 500)
blue = (0, 0, 255)
screen = pg.display.set_mode(reso)

plane = pg.image.load('plane.jpg')
plane = pg.transform.scale(plane, (150, 60))
planerect = plane.get_rect()

xs = 75
ys = 250
vx = 50
tsim = 0.0
tstart = 0.001 * pg.time.get_ticks()
dt = 0.01
running = True

## DRAWING CODE BLOCK
while running:
    # update current time
    trun = 0.001 * pg.time.get_ticks() - tstart
    # Perform update when dt time has elapsed
    if trun + dt >= tsim:
        tsim = tsim + dt
        xs = xs + vx * dt
        planerect.center = (xs, ys)

    # Event pump to keep the window responsive
    pg.event.pump()

    screen.fill(blue)
    screen.blit(plane, planerect)

    pg.display.flip()

    # Add a terminating condition for when the
    # airplane leaves the screen
    if xs > 750 + 75:
        running = False

# Quit after the loop finishes
pg.quit()