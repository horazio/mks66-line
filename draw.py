from display import *

def draw_line(x0, y0, x1, y1, screen, color):
    if(x1 < x0):
        x1, x0 = x0, x1
        y1, y0 = y0, y1
    if(y1 - y0 > 0):
        if(x1 - x0 > y1 - y0):
            oct = 2
        else:
            oct = 1
    else:
        if(x1 - x0 > y0 - y1):
            oct = 3
        else:
            print("ppf\n")
            oct = 4

    line( x0, y0, x1, y1, screen, color, oct)



def line(x0, y0, x1, y1, screen, color, oct):
    x = x0
    y = y0

    A = y1 - y0
    B = x0 - x1

    if(oct == 2 or oct == 3):
        d = 2 * A + B
    else:
        d = 2 * B + A

    while( x < x1):
        plot(screen, color, x,y)
        if(oct == 1):
            if(d < 0):
                x += 1
                d += 2 * A
            y += 1
            d += 2 * B
        if(oct == 2):
            if(d > 0):
                y += 1
                d += 2 * B
            x += 1
            d += 2 * A
        if(oct == 3):
            if(d < 0):
                y -= 1
                d -= 2 * B
            x += 1
            d += 2 * A
        if(oct == 4):
            if(d > 0):
                x += 1
                d += 2 * A
            y -= 1
            d -= 2 * B
