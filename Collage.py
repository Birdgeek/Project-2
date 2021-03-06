from java.util import Random #Used for star generation


def collage():
  #Written by Brad Snurka
  #10/4/16 - 10/17/16
  #Ver 1.0
  #This project has been tracked on github @ https://github.com/Birdgeek/Project-2
  
  canvas = makeEmptyPicture(700, 515, black) #Make our empty canvas

   #Individual picture creation - Must use "setMediaPath()" before hand
   
  signaturePic = makePicture(getMediaPath("signature.jpg"))
  sun = makePicture(getMediaPath("volleyball.png"))
  mercury = makePicture(getMediaPath("planet.png"))
  venus = makePicture(getMediaPath("planet.png"))
  earth = makePicture(getMediaPath("earth.jpg"))
  mars = makePicture(getMediaPath("planet.png"))
  jupiter = makePicture(getMediaPath("planet.png"))
  saturn = makePicture(getMediaPath("planet.png"))
  uranus = makePicture(getMediaPath("planet.png"))
  neptune = makePicture(getMediaPath("planet.png"))
  
  #Actual creation of the collage
  
  makeStars(canvas)
  placeSun(sun, canvas)
  placeMercury(mercury, canvas)
  placeVenus(venus, canvas)
  placeEarth(earth, canvas)
  placeMars(mars, canvas)
  placeJupiter(jupiter, canvas)
  placeSaturn(saturn, canvas)
  placeUranus(uranus, canvas)
  placeNeptune(neptune, canvas)
  signature(signaturePic, canvas) #Writes my signature to canvas in upper right - Should be last thing to be done
  explore(canvas)
  
  #Indivdual Planets functions

def makeStars(target):
  for px in getPixels(target):
    rand = Random()
    value = rand.nextInt(125) #.008% chance of a pixel become a star pixel
    if (value == 7):
      setColor(px, pickStarColor())
   

def placeSun(sun, target):
  sun = scaleDown(sun, 2)
  yellowrize(sun)
  copy(sun, 161, 66, 250, 236, 0, (getHeight(target)/2) - (236/2), 57, 51, 29, target)
	
def placeMercury(src, target):
  src = scaleDown(src, 16)
  brownerize(src)
  copy(src, 1, 1, 24, 18, 144, 236, 153, 153, 51, target)
	
def placeVenus(src, target):
  src = scaleDown(src, 10)
  src = grayscale(src)
  copy(src, 1, 1, 39, 29, 200, 236, 255, 255, 255, target)

def placeEarth(src, target):
  src = scaleDown(src, 6)
  copy(src, 1, 1, 45, 45, 273, 236, 255, 255, 255, target)
  
def placeMars(src, target):
  src = scaleDown(src, 9)
  for i in range(2):
    src = blur(src)
  copyColor(src, 1, 1, 43, 32, 341, 236, 255, 255, 255, target, makeColor(186, 102, 24))
	
def placeJupiter(src, target):
  src = scaleDown(src, 5)
  mirrorHoriz(src)
  swap(src)
  swap(src)
  chromaColor(src, 91, 104, 25, makeColor(110, 35, 69))
  copy(src, 1, 1, 79, 60, 416, 220, 255, 255, 255, target)
  
def placeSaturn(src, target):
  src = scaleDown(src, 7)
  swap(src)
  mirrorVert(src)
  copy(src, 1, 1, 56, 42, 514, 220, 255, 255, 255, target)
  
def placeUranus(src, target):
  src = scaleDown(src, 10)
  mirrorVert(src)
  cyanotype(src)
  copy(src, 1, 1, 39, 29, 590, 220, 255, 255, 255, target)
	
def placeNeptune(src, target):
  src = scaleDown(src, 10)
  swap(src)
  cyanotype(src)
  swap(src)
  swap(src)
  copy(src, 1, 1, 39, 29, 640, 220, 255, 255, 255, target)
  
  
  #Functions Used
  
  #Copys a picture from one picture to another ingoring a certain color
def copy(src, startX, startY, endX, endY, locX, locY, red, green, blue, target):
  #Copies from input picture from Start-end px and puts it to the target in corresponding location
  storeY = locY
  for x in range(startX, endX):
    for y in range(startY, endY):
      px = getPixel(src, x, y)
      if (getRed(px) != red) and (getGreen(px) != green) and (getBlue(px) != blue):
        color = getColor(getPixel(src, x, y))
        setColor(getPixel(target, locX, locY), color)
      locY = locY + 1
    locX = locX + 1
    locY = storeY
    
  #Copys a chunk from one picture to another, also paints the whole thing to be copied to a unified color
def copyColor(src, startX, startY, endX, endY, locX, locY, red, green, blue, target, color):
  #Copies from input picture from Start-end px and puts it to the target in corresponding location
  storeY = locY
  for x in range(startX, endX):
    for y in range(startY, endY):
      px = getPixel(src, x, y)
      if (getRed(px) != red) and (getGreen(px) != green) and (getBlue(px) != blue):
        setColor(getPixel(target, locX, locY), color)
      locY = locY + 1
    locX = locX + 1
    locY = storeY
    
  #Returns random star looking color
def pickStarColor():
  rand = Random()
  value = rand.nextInt(50)
  if (value == 7) or (value == 15):
    return blue
  elif (value == 8) or (value == 42):
    return yellow
  elif (value == 9) or (value == 32):
    return makeColor(127, 174, 255)
  elif (value == 22) or (value == 30):
    return makeColor(255, 176, 127)
  elif (value == 25) or (value == 26):
    return makeColor(170, 121, 216)
  elif (value == 18) or (value == 4):
    return makeColor(156, 216, 121)
  elif (value == 12) or (value == 24):
    return makeColor(216, 204, 121)
  else:
    return white
  
  #Gradually blurs a picture
  #Can be run multiple times in a loop to blue a lot    
def blur(src):
  target = duplicatePicture(src)
  for x in range(1, getWidth(src)-1):
    for y in range(1, getHeight(src)-1):
      top = getPixel(src, x, y-1)
      left = getPixel(src, x-1, y)
      bottom = getPixel(src, x, y+1)
      right = getPixel(src, x+1, y)
      center = getPixel(target, x, y)
      
      newRed = (getRed(top) + getRed(left) + getRed(bottom) + getRed(right) + getRed(center))/5
      newGreen = (getGreen(top) + getGreen(left) + getGreen(bottom) + getGreen(right) + getGreen(center))/5
      newBlue = (getBlue(top) + getBlue(left) +getBlue(bottom) + getBlue(right) + getBlue(center))/5
      
      setColor(center, makeColor(newRed, newGreen, newBlue))
  return target
  
  #Scales a picture down from its original size to a new size as determined by scale factor  
def scaleDown(src, scaleFactor):
  newSize = makeEmptyPicture(getWidth(src)/int(scaleFactor), getHeight(src)/int(scaleFactor))
  sourceX = 0
  for x in range(0,getWidth(src)/scaleFactor):
    sourceY = 0
    for y in range(0, getHeight(src)/scaleFactor):
      setColor(getPixel(newSize, x, y), getColor(getPixel(src, sourceX, sourceY)))
      sourceY = sourceY + scaleFactor
    sourceX = sourceX + scaleFactor
  return newSize
  
  #Mirrors the first quarter of a picture to the opposite quarter
def mirrorVert(src): 
  mirrorPoint = getWidth(src)/2
  width = getWidth(src)
  for y in range(0, getHeight(src)):
    for x in range(0,mirrorPoint):
      leftpx = getPixel(src, x, y)
      rightpx = getPixel(src, width - x -1, y)
      color = getColor(leftpx)
      setColor(rightpx, color)
  return src 

  #Mirrors the top half to the bottom half
def mirrorHoriz(src):
  mirrorPoint = getHeight(src)/4
  height = getHeight(src)
  for x in range(0, getWidth(src)):
    for y in range(0 , mirrorPoint):
      toppx = getPixel(src, x, y)
      bottompx = getPixel(src, x, height - y -1)
      color = getColor(toppx)
      setColor(bottompx, color)
  return src
  
  #Returns luminance of a pixel
def luminance(pixel):
  r = getRed(pixel)
  g = getGreen(pixel)
  b = getBlue(pixel)
  return (r+g+b)/3
  
  #Gradually sets all colors of all pictures towards yellow
def yellowrize(src):
  for px in getPixels(src):
    setColor(px, makeColor(getRed(px) * 1.5, getGreen(px) * 1.5, getBlue(px) * .3))
  return src
  
  #Gradually shifts all pixels towards brown
def brownerize(src):
  for px in getPixels(src):
    if (getRed(px) < 114):
      setColor(px, makeColor(getRed(px) * 1.2, getGreen(px) * 1.2, getBlue(px) * .2))
    else:
      setColor(px, makeColor(getRed(px) * .6, getGreen(px) * .6, getBlue(px) * .2))
  
  #Converts a given picture to blue cyanotype
def cyanotype(src):
  grayscale(src)
  for px in getPixels(src):
    blue = getBlue(px)
    if (blue < 63):
      setBlue(px, (blue*2))
    elif (63 < blue <= 191):
      setBlue(px, (blue * 1.3))
    elif (blue > 191):
      setBlue(px,(blue * 1.2))
    setGreen(px,(getGreen(px) * .75))
    setRed(px,(getRed(px) * .75))
  return src  
  
  #Converts picture to grayscale
def grayscale(src):
  for p in getPixels(src):
    intensity = luminance(p)
    setColor(p, makeColor(intensity, intensity, intensity))
  return src
  
  #Performs a color swap on a picture
  #Red become Blue
  #Green becomes Red
  #Blue becomes Green
def swap(src):
  for p in getPixels(src):
    red = getRed(p)
    green = getGreen(p)
    blue = getBlue(p)
    setColor(p, makeColor(blue, red, green))
  return src
  
  #Sets color of a single color, to a different color. - I.E. All 255,255,255 turning to 127,127,127
def chromaColor(src, red, green, blue, newColor):
  for px in getPixels(src):
    if ((getRed(px) == red) and (getGreen(px) == green) and (getBlue(px) == blue)):
      setColor(px, newColor)
  return src

  #Chromakey function used to copy the sun by ignoring the background
def chromakeySun(src, target):
  for px in getPixels(src):
    x = getX(px)
    y = getY(px)
    if ((getRed(px) > 230) and (getGreen(px) > 230) and (getBlue(px) < 100)):
      bgpx = getPixel(target, x, y)
      bgcol = getColor(src)
      setColor(px, bgcol)
			
  #Writes my signature at a scale of 1/10th to the canvas
def signature(src, target):
  src = scaleDown(src, 10)
  for px in getPixels(src):
    if (getRed(px) < 50) and (getGreen(px) < 50) and (getBlue(px) < 50):
      srcColor = white
      trgLoc = getPixel(target, getX(px), getY(px))
      setColor(trgLoc, srcColor)
  return target