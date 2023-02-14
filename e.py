import os
import keyboard as kb

height = (os.get_terminal_size().lines)
space = 0
y = 1
placeholder = [ " " * height ]

map = placeholder + [ 
        "   |  |",
        "   |  |",
        "    ___"
] 

def space_out(mapp):
    map2 = []
    for i in mapp:
        map2 = map2 + [i + " " * (height - len(i))]
    return map2

map = space_out(map)

def update():
    for i in range(0, height):
        if i == y:
            if i < len(map):
                print( map[i][0:space] + "*" + map[i][space + 1:len(map[i])])
            else:
                print( " " * space + "*" )
        elif i < len(map):
            print(map[i])
        elif i >= len(map):
            print(" ")

def movey(e):
    if e == 1:
        y += 1
    else:
        y -= 1

def movex(e):
    if e == 1:
        space += 1
    else:
        space -= 1

while True:
    update()
    # inpoot = input()
    if kb.is_pressed("d"):
        space += 1
    elif kb.is_pressed("s"):
        y += 1
    elif kb.is_pressed("a"):
        space -= 1
    elif kb.is_pressed("w"):
        y -= 1
    elif kb.is_pressed("q"):
        break
