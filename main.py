from display import *
from draw import *

screen = new_screen()
color = [ 0, 255, 0 ]

i = 0
j = 500
while(i < 500):
    draw_line(i, 0, 0, j, screen, [i, j, 200])
    draw_line(i, j, 500, 500, screen, [i, j, 200])
    draw_line(i, j, 150, 150, screen, [i, j, 200])
    draw_line(i, j, 350, 350, screen, [i, j, 200])
    i += 10
    j -= 10

display(screen)
save_extension(screen, 'img.png')
