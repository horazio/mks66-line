from display import *
from draw import *

screen = new_screen()
color = [ 0, 255, 0 ]

x = -50;
while(x < 500):
    i = 0
    j = 500
    while(i < 500):
        draw_line(i + x, 0 + x, 0 + x, j + x, screen, [i, j, 200])
        #draw_line(i + x, j + x, 500 + x, 500 + x, screen, [i, j, 200])
        #draw_line(i + x, j + x, 150 + x, 150 + x, screen, [i, j, 200])
        #draw_line(i + x, j + x, 350 + x, 350 + x, screen, [i, j, 200])
        i += 10
        j -= 10
    x += 50


display(screen)
save_extension(screen, 'img.png')
