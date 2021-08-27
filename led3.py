#=================================
#    PGZs LEDs
#    Aug 17, 2021
# -------------------
#================================

import board
import neopixel
import time
import random

#Pin 18 on RPI
pixel_pin = board.D18

#Number of LEDS... I have 300 on the strip
num_pixels = 17*17

xLen = 17
yLen = 17

pacRuns = 0
alt = False
alt2 = False
#Initialize the pixels 
pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=0.5, auto_write=False)

#Color Wheel function. Simplifies choosing a color
def wheel(pos):
  #Input a color 0 to 255 to get a color
  #The Colors are a transition r - g - b back to r.
  if pos < 0 or pos > 255:
    return (0, 0, 0)
  if pos < 85:
    return (255 - pos * 3, pos * 3, 0)
  if pos < 170:
    pos -= 85
    return(0, 255 - pos * 3, pos * 3)
  pos -= 170
  return (pos * 3, 0, 255 - pos * 3)


#====================================
#   CLEAR GRID
#====================================
def clearGrid():
  pixels.fill((0,0,0))
  pixels.show()

def clearPix(xPos, yPos):
  pixels[grid(xPos,yPos)] = ((0,0,0))
#======================================================================
#   GRID - Return the position on the strip of the passed in x,y coord
#======================================================================
def grid(xpos, ypos):
  pixloc = 0
  pixloc = pixloc + (ypos*17)
  #If this is an odd row, its reversed

  if ypos % 2 > 0:
    pixloc += (16-xpos)
  else:
   pixloc += xpos
  return pixloc


#===========================================
#         Color Cycle (real original)
#===========================================
def colorCycle():
  #Cycle all the colors
  color = 0
  for k in range(25):
    color = color + 10
 
    for i in range(17):
      for j in range(17):
        loc = grid(j,i)
        pixels[loc] = wheel(color)
    pixels.show()
    time.sleep(0.1) 

#=============================================
#        Rainbow Stuff :) (pride month)
#=============================================
def rainbowStuff():
  #Do Rainbow stuff
  for k in range(30):
    for i in range(17):
      for j in range(17):
        loc = grid(j,i)
        pixels[loc] = wheel(random.randint(0,255))
      pixels.show()


  #clearGrid()
  #time.sleep(1)

#================================================
#        Triforce :) .... Newguys cant?
#================================================
def triForce():
 for z in range(3):
  for k in range(10):
    for i in range(17):
      for j in range(17):
        pixels[grid(i,j)] = ((0,0,0))

    for i in range(4):
      more = i
      pixels[grid(8,i+k)] = wheel(40)
      while more > 0 and (i+k<17):
        pixels[grid(8+more,i+k)] = wheel(40)
        pixels[grid(8-more,i+k)] = wheel(40)
        more -= 1

    for i in range(4):
      more = i
      pixels[grid(4,i+4+k)] = wheel(40)
      while more > 0 and (i+k<17):
        pixels[grid(4+more,i+4+k)] = wheel(40)
        pixels[grid(4-more,i+4+k)] = wheel(40)
        more -= 1

    for i in range(4):
      more = i
      pixels[grid(12,i+4+k)] = wheel(40)
      while more > 0 and (i+k<17):
        pixels[grid(12+more,i+4+k)] = wheel(40)
        pixels[grid(12-more,i+4+k)] = wheel(40)
        more -= 1

    pixels.show()
    time.sleep(0.1)
    #clearGrid()

def white():
  return (200,200,200)


#===================================================
#                Pacman stuff!
#==================================================
def pacman(bcolor, pacRuns, alt, alt2):
  #clearGrid() - Always call this before the pacman run

  #bcolor will be passed in for max trippiness
  row = 1
  offset = 0


  #These ones should stay the same... for now 
  #Top Row
  for i in range (6,11):
    pixels[grid(i,row)] = wheel(bcolor)
  row +=1

  #Second Row
  for i in range (4,13):
    pixels[grid(i,row)] = wheel(bcolor)
  row +=1

  #Third Row
  for i in range (3,14):
    pixels[grid(i,row)] = wheel(bcolor)
  row += 1

  #Fourth - Sixth
  for i in range (2,15):
    for j in range(3):
      pixels[grid(i,row+j)] = wheel(bcolor)
  row += 3

  #Sixth -  Thirteen
  for i in range (1,16):
    for j in range(7):
      pixels[grid(i,row+j)] = wheel(bcolor)
  row += 7


  #================================================
  #This is the variable part. Yuck
  #================================================
  if pacRuns % 50 == 0:
    if alt2 == True:
      alt2 = False
    else:
      alt2 = True
    for i in range (0,16):
      for j in range (14,16):
        clearPix(i,j)

  if pacRuns % 100 == 0:
    if alt == True:
      alt = False
    else:
      alt = True

    #clear the eyes and the skirt
    for i in range (4,6):
      for j in range (7,9):
        pixels[grid(i+offset,j)] = white()

  #===============================================
  if alt2 == False:
    #2nd to last Row
    for i in range (1,5):
      pixels[grid(i,row)] = wheel(bcolor)

    for i in range (6,11):
      pixels[grid(i,row)] = wheel(bcolor)

    for i in range (12,16):
      pixels[grid(i,row)] = wheel(bcolor)

    row += 1

    #Last Row
    for i in range (2,4):
      pixels[grid(i,row)] = wheel(bcolor)

    for i in range (7,10):
      pixels[grid(i,row)] = wheel(bcolor)

    for i in range (13,15):
      pixels[grid(i,row)] = wheel(bcolor)

  #Alternative Skirt ....
  elif alt2 == True:
    for i in range (1,4):
      pixels[grid(i,row)] = wheel (bcolor)
    for i in range (5,8):
      pixels[grid(i,row)] = wheel (bcolor)
    for i in range (10,13):
      pixels[grid(i,row)] = wheel (bcolor)
    for i in range (14,16):
      pixels[grid(i,row)] = wheel (bcolor)

    row += 1
    for i in range (1,3):
      pixels[grid(i,row)] = wheel (bcolor)
    for i in range (6,8):
      pixels[grid(i,row)] = wheel (bcolor)
    for i in range (10,12):
      pixels[grid(i,row)] = wheel (bcolor)
    pixels[grid(15,row)] = wheel(bcolor)

  #Eyes.. Offset is used to draw the 2nd one
  #2 eyes - Inner Lines
  for k in range (2):
    #Xcoords
    for i in range (5,7):
      #Ycoords
      for j in range (5):
        pixels[grid(i+offset,j+5)] = white()

    #Outside(wider) part
    for i in range (4,8):
      for j in range (3):
        pixels[grid(i+offset,j+6)] = white()

    if alt == False:
      #Pupil
      for i in range (4,6):
        for j in range (7,9):
          pixels[grid(i+offset,j)] = wheel(150)
    else:
      for i in range (6,8):
        for j in range (7,9):
          pixels[grid(i+offset,j)] = wheel(150)

    offset += 5
  pixels.show()
  return(alt, alt2)
  #time.sleep(0.5)



#=====================================
#   WAR What is it good for
#=====================================

def war():
  clearGrid()
  gameOver = False
  turn = 1

  #Initial Setup
  pixels[grid(0,0)] = wheel(10)
  pixels[grid(0,16)] = wheel(50)
  pixels[grid(16,16)] = wheel(100)
  pixels[grid(16,0)] = wheel(200)
  pixels.show()



##=========================================
## Main program ... show your stuff!
##=========================================
while True:

  # 1 War 
#  war()

  # 2 Pacman!
  clearGrid()
  for j in range (10):
    for i in range (25):
      (alt,alt2) = pacman(i*10,pacRuns, alt,alt2)
      pacRuns+=1

  clearGrid()
  for j in range (10):
    for i in range (25):
      (alt,alt2) = pacman(10,pacRuns, alt,alt2)
      pacRuns+=1


  # 3 Triforce
  triForce()


  # 4 colorCycle()
  rainbowStuff()
