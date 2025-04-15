import os
import sys
tilenumb = ["1","2","3","4","5"]
tiletype = ["a","b","c","d","e","f", "g"]
emptytile = "[   ]"
filledtile = "[ * ]"
playertile = "[ / ]"
currenttile = 0
currenttileselected = ""
tileplayerdata = [
    "c3",
]
tiledata = [
]

map1 = [
  "a1",
  "a5",
  "g1",
  "g5",
  "c2",
  "b2",
  "d2",
  "e2",
  "f2",
  "f1",
  "b1",
  "c4",
  "b4",
  "d4",
  "e4",
  "f4",
  "f5",
  "b5",
]

map2 = [
 "a2",
 "b2",
 "c2",
 "d2",
 "e2",
 "f2",
 "g2",
 "a4",
 "b4",
 "c4",
 "d4",
 "e4",
 "f4",
 "g4",
]

def clrcon():
    if sys.platform == "win32":
        os.system("cls")
    else:
        os.system("clear")

def mapload(map, enter, direction):
    tiledata.clear()
    if map == "map1":
        for y in map1:
            tiledata.append(y)
    if map == "map2":
        for y in map2:
            tiledata.append(y)
    if map == "clear":
        print("Cleared")
    tileplayerdata.pop(0)
    if enter == True:
        if direction == "Front":
            tileplayerdata.append("a3")
        elif direction == "Back":
            tileplayerdata.append("g3")
    else:
        tileplayerdata.append("c3")
        
    clrcon()

def array_find(array, value, bool):
    for x in range(len(array)):
        if array[x] == value:
            if bool == True:
                return True
            else:
                return x
            
def drawtile(filled, border):
    if border == False:
        if filled == "Normal":
            print(filledtile, end = "")
        elif filled == "Player":
            print(playertile, end = "")
        elif filled == "Nil":
            print(emptytile, end = "")
    else:
        if filled == "Normal":
            print(filledtile)
        elif filled == "Player":
            print(playertile)
        elif filled == "Nil":
            print(emptytile)
            
def getmapbound(array, data):
    if array:
        if data < len(array):
            return True
            
def switchtiledata(data, array, type):
    clrcon()
    if type == "up":
        w = list(data)
        nw = tiletype[array_find(tiletype, w[0], False) - 1]
        blocked = array_find(tiledata, nw + w[1], True)
        if blocked == True:
            print("Path is blocked")
        else:
            array.remove(data)
            array.append(nw + w[1])
    if type == "down": #need to add map bound same for this
        w = list(data)
        mapbound = getmapbound(tiletype, array_find(tiletype, w[0], False) + 1)
        if mapbound == True:
            nw = tiletype[array_find(tiletype, w[0], False) + 1]
            blocked = array_find(tiledata, nw + w[1], True)
            if blocked == True:
                print("Path is blocked")
            else:
                array.remove(data)
                array.append(nw + w[1])
        else:
            array.pop(0)
            array.append("a" + w[1])
    if type == "right": #need to add map bound
        w = list(data)
        mapbound = getmapbound(tilenumb, array_find(tilenumb, w[1], False) + 1)
        if mapbound == True:
            nw = tilenumb[array_find(tilenumb, w[1], False) + 1]
            blocked = array_find(tiledata, w[0] + nw, True)
            if blocked == True:
                print("Path is blocked")
            else:
                array.remove(data)
                array.append(w[0] + nw)
        else:
            array.pop(0)
            array.append(w[0] + "1")
    if type == "left":
        w = list(data)
        nw = tilenumb[array_find(tilenumb, w[1], False) - 1]
        blocked = array_find(tiledata, w[0] + nw, True)
        if blocked == True:
            print("Path is blocked")
        else:
            array.remove(data)
            array.append(w[0] + nw)
           
     
def movetile(array, arraynumb, move):
    switchtiledata(array[arraynumb], array, move)
            
def checktile(numbrow, selectedtile):
    tilecheck = array_find(tiledata, selectedtile, True)
    tileplayercheck = array_find(tileplayerdata, selectedtile, True)
    if numbrow == len(tilenumb):
        if tilecheck == True:
            drawtile("Normal", True)
        elif tileplayercheck == True:
            drawtile("Player", True)
        else:
            drawtile("Nil", True)
    else:
        if tilecheck == True:
            drawtile("Normal", False)
        elif tileplayercheck == True:
            drawtile("Player", False)
        else:
            drawtile("Nil", False)

def refreshvisual():
    for x in range(len(tiletype)):
        currenttile = tiletype[x]
        for y in range(len(tilenumb)):
            currenttileselected = currenttile + str(y + 1)
            checktile(y + 1, currenttileselected)

def realinput():
    x = input()
    sep = x.split()
    loadcom = array_find(sep, "load", True)
    if x == "up":
        movetile(tileplayerdata, 0, "up")
        refreshvisual()
    if x == "down":
        movetile(tileplayerdata, 0, "down")
        refreshvisual()
    if x == "left":
        movetile(tileplayerdata, 0, "left")
        refreshvisual()
    if x == "right":
        movetile(tileplayerdata, 0, "right")
        refreshvisual()   
    if loadcom == True:
        print(sep[1])
        mapload(sep[1], False, "Nil")
        refreshvisual()
    realinput()
         
refreshvisual()
realinput()