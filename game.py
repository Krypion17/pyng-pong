import time
import os
import getch
from kbhit import KBHit
import random as rand

height, width = os.get_terminal_size().lines, os.get_terminal_size().columns
padlen = height // 5
y , y1 = (height // 2) + padlen // 2, (height // 2) + padlen // 2

px, py, vx, vy = width // 2, rand.randint(1, height - 1), 1, 1
score1, score2 = 0, 0

kb = KBHit()
while True:
    stre = ""
    for i in range(height):
        if i >= y and i <= (y + padlen):
            stre = " "*(width // 5) + "|" + " "*((width * 3)//5) # + "|" + " "*((width // 5))
        else:
            stre = " "*width

        if i >= y1 and i <= (y1 + padlen):
            stre = stre[:(width * 4) // 5] + "|" + " "*((width // 5))
        else:
            stre = stre[:(width * 4) // 5] + " "*(width//5)

        if i == 2:
            stre = stre[:((width * 5)//11)-2] + str(score1 // 10) + str(score1 % 10) + stre[(width * 5)//11:((width * 6)//11)-2] + str(score2 // 10) + str(score2 % 10) + stre[(width*6)//11:]

        if i == py:
            stre = stre[:px] + "o" + stre[px + 1:]

        print(stre)
    time.sleep(0.1)

    if py >= height - 1 or py <= 1:
        vy *= -1
        px += vx
        py += vy
    else:
        px += vx
        py += vy
    if (px == ((width // 5) + 1) and (py >= y and py <= (y + padlen))) or (px == ((width * 4 // 5) - 1) and (py >= y and py <= (y + padlen))):
        vx *= -1
        px += vx
        py += vy
    else:
        px += vx
        py += vy
    if px < (width // 5) - 1:
        px, py = width // 2, rand.randint(1, height - 1)
        if score2 == 10:
            print("Player 2 wins!")
            break
        score2 += 1
    elif px > (width * 4 // 5) + 1: # or px <= (width // 5) + 1:
        px, py = width // 2, rand.randint(1, height - 1)
        if score1 == 10:
            print("Player 1 wins!")
            break
        score1 += 1

    if kb.kbhit():
        inp = getch.getch()
        if inp == "s" and y + padlen < height:
            y += 1
        elif inp == "w" and y > 0:
            y -= 1
        elif inp == '\x1b':
            inp = getch.getch()
            inp = getch.getch()
            if inp == "A" and y1 > 0:
                y1 -= 1
            elif inp == "B" and y1 + padlen < height:
                y1 += 1
        elif inp == "q":
            break
