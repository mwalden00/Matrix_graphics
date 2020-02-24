from display import *
from draw import *
from matrix import *
import math

screen = new_screen()
color = [ 0, 255, 0 ]
matrix = new_matrix()

print("Testing add_edge. adding (1,2,3), (4,5,6) m2 =")
m2 = new_matrix(0,0)
add_edge(m2,1,2,3,4,5,6)
print_matrix(m2)

print("\nTesting ident. m1 =")
m1 = new_matrix()
ident(m1)
print_matrix(m1)

print("\nTesting Matrix mult. m1 * m2 =")
m2 = matrix_mult(m1,m2)
print_matrix(m2)

print("\nTesting Matrix mult. m1 =")
n = 1
for col in m1:
    for i in range(len(col)):
        if i == 3:
            col[i] = 1
        else:
            col[i] = n
            n += 1
print_matrix(m1)

print("\nTesting Matrix mult. m1 * m2 =")
m2 = matrix_mult(m1,m2)
print_matrix(m2)

print("\n#======================================================================#")

print("\nMaking image:\nAdding edges...")

m4 = m3 = m2 = m1 = new_matrix(0,0)
cy = cx = XRES/2

deg = math.pi / 180
theta = n = 0

add_edge(m1,0,250,0,250,YRES-1,0)
add_edge(m1,250,YRES-1,0,XRES-1,250,0)
add_edge(m1,XRES-1,250,0,250,0,0)
add_edge(m1,250,0,0,0,250,0)

while True:
    x1 = int(cx + XRES/3 * math.cos(theta*deg))
    y1 = int(cy + YRES/3 * math.sin(theta*deg))
    x2 = int(cx + XRES/3 * math.cos((theta + 165)*deg))
    y2 = int(cy + YRES/3 * math.sin((theta + 165)*deg))
    if n % 4 == 0:
        n+=1
        add_edge(m1,x1,y1,0,x2,y2,0)
    if n % 4 == 1:
        n+=1
        add_edge(m2,x1,y1,0,x2,y2,0)
    if n % 4 == 2:
        n+=1
        add_edge(m3,x1,y1,0,x2,y2,0)
    if n % 4 == 3:
        add_edge(m4,x1,y1,0,x2,y2,0)
        n = 0
    theta += 13
    if theta % 360 == 0:
        break

print("Drawing lines...")

draw_lines( m1, screen, [255,0,0] )
draw_lines( m2, screen, [0,255,0] )
draw_lines( m3, screen, [0,0,255] )
draw_lines( m4, screen, [255,255,255] )

print("Done!")
display(screen)
