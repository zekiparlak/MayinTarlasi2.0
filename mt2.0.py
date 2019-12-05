import random
import time
import os
point = 0
count = 0
win = False
message = False
def MAP():
	for i in range(7):
		for j in range(7):
			print(map[i][j]," ",end="",flush=True)
		print()
def move(x,y):
    global point
    global count
    global message
    global win
    mvx = 0
    mvy = 0
    over = True
    for i in range(7):
        for j in range(7):
            if map[i][j] == "X":
                mvx = i
                mvy = j
    mvx = mvx + x
    mvy = mvy + y
    if map[mvx][mvy] == "W":
        win = True
    if ((mvx<=5)and(mvx>=1))and((mvy<=5)and(mvy>=1)):
        if map[mvx][mvy] == "O" or map[mvx][mvy] == "!":
            point += 1
            if point == 21:
                map[0][3] = "W"
            if map[1][2] == "!" and map[1][3] == "!" and map[1][4] == "!":
                message = True
            if point%5 == 0 and point<=15:
                count += 1
                map[mrx[count][0]][mrx[count][1]] = "!"
            if (mvx == mrx[1][0] and mvy == mrx[1][1]) or (mvx == mrx[2][0] and mvy == mrx[2][1]) or (mvx == mrx[3][0] and mvy == mrx[3][1]):
                map[mvx][mvy] = "~"
                map[mvx - x][mvy - y] = " "
                os.system("clear")
                print("MAYIN TARLASI 2.0\nCreated by freeNULL")
                print()
                print("Puan:",point)
                print()
                MAP()
                print("BOOOMMM\nGAME OVER")
                over = False
                return over
        map[mvx][mvy] = "X"
        map[mvx - x][mvy - y] = " "
while True:
    point = 0
    count = 0
    map = [["#","#","#","#","#","#","#"],
		   ["#","O","O","O","O","O","#"],
		   ["#","O","O","O","O","O","#"],
		   ["#","O","O","O","O","O","#"],
		   ["#","O","O","O","O","O","#"],
		   ["#","O","O","O","O","O","#"],
		   ["#","#","#","#","#","#","#"]]
    count2 = 0
    mrx = [[0 for x in range(2)] for y in range(4)]
    while count2 < 4:
        x = random.randint(1,5)
        y = random.randint(1,5)
        mrx[count2][0] = x
        mrx[count2][1] = y
        for i in range(count2):
            if (mrx[count2][0] == mrx[i][0]) and (mrx[count2][1] == mrx[i][1]):
                count2 -= 1
        count2 += 1
    map[mrx[0][0]][mrx[0][1]] = "X"
    game = True
    while game:
        os.system("clear")
        #for i in range(4):             $Hile
            #print(mrx[i][0],mrx[i][1])	$Hile
        if win == True:
            print("You Win")
            win = False
            break
        print("MAYIN TARLASI 2.0\n")
        print()
        print("Puan:",point)
        print()
        MAP()
        print()
        print("LEFTUP:7   UP:8   RIGHTUP:9")
        print("LEFT:4:           RIGHT:6")
        print("LEFDOWN:1  DOWN:2 RIGHTDOWN:3")
        print()
        if message == True:
            print("BOKU YEDİN HAHAHAHAHAHA")
        cmove = int(input("move:"))
        if cmove == 8:
            if move(-1,0) == False:
                print("Puan:",point)
                break
        elif cmove == 6:
            if move(0,1) == False:
                print("Puan:",point)
                break
        elif cmove == 4:
            if move(0,-1) == False:
                print("Puan:",point)
                break
        elif cmove == 2:
            if move(1,0) == False:
                print("Puan:",point)
                break
        elif cmove == 7:
            if move(-1,-1) == False:
                print("Puan:",point)
                break
        elif cmove == 9:
            if move(-1,1) == False:
                print("Puan:",point)
                break
        elif cmove == 1:
            if move(1,-1) == False:
                print("Puan:",point)
                break
        elif cmove == 3:
            if move(1,1) == False:
                print("Puan:",point)
                break	
    time.sleep(3)
