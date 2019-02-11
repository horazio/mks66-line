from display import *

def draw_line(x0, y0, x1, y1, screen, color):
    if(x1 < x0):
        x1, x0 = x0, x1
        y1, y0 = y0, y1

    x = x0
    y = y0

    A = y1 - y0
    B = x0 - x1


    if(y1 - y0 > 0):
        if(x1 - x0 > y1 - y0):
            line( x0, y0, x1, y1, screen, color)
        else:
            line_vert(x0, y0, x1, y1, screen, color)
    else:
        if(x1 - x0 > y0 - y1):
            down(x0, y0, x1, y1, screen, color)
        else:
            down_vert(x0, y0, x1, y1, screen, color)
            pass


def line(A,B, x, y, x1, y1, screen, color ):

    d = 2 * A + B

    while( x < x1):
        plot(screen, color, x,y)
        if(d > 0):
            y += 1
            d += 2 * B
        x += 1
        d += 2 * A

def line_vert( x0, y0, x1, y1, screen, color ):

     if(x1 < x0):
        x1, x0 = x0, x1
        y1, y0 = y0, y1

    d = 2 * B + A

    while( y < y1):
        plot(screen, color, x,y)
        if(d < 0):
            x += 1
            d += 2 * A
        y += 1
        d += 2 * B

def down(x0, y0, x1, y1, screen, color):


    d = 2 * A + B

    while( x < x1):
        plot(screen, color, x,y)
        if(d < 0):
            y -= 1
            d -= 2 * B
        x += 1
        d += 2 * A


def down_vert(x0, y0, x1, y1, screen, color):

    d = 2 * B + A

    while( x < x1):
        plot(screen, color, x,y)
        if(d > 0):
            x += 1
            d += 2 * A
        y -= 1
        d -= 2 * B
