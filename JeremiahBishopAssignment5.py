# 1

def decreaseRed(picture, percentage):
  for p in getPixels(picture):
    value = getRed(p)
    setRed(p, value*percentage)
    

def decreaseGreen(picture, percentage):
  for p in getPixels(picture):
    value = getGreen(p)
    setGreen(p, value * percentage)    


def decreaseBlue(picture, percentage):
  for p in getPixels(picture):
    value = getBlue(p)
    setBlue(p, value * percentage)


def changeImageToBlack(picture):
  for p in getPixels(picture):
    setRed(p, 0)
    setBlue(p, 0)
    setGreen(p, 0)

def greenify(picture):
  for p in getPixels(picture):
    setRed(p, getRed(p) * 0.75)
    setGreen(p, 255)
    setBlue(p, getBlue(p) * 0.75)

file = pickAFile()
myPicture = makePicture(file)
explore(myPicture)
#changeImageToBlack(myPicture)
greenify(myPicture)
explore(myPicture)