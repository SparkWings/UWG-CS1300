# 1.1 #
def decreaseRed(picture):
  for p in getPixels(picture):
    value = getRed(p)
    setRed(p, value*0.5)
    

def decreaseGreen(picture):
  for p in getPixels(picture):
    value = getGreen(p)
    setGreen(p, value * 0.3)    


def decreaseBlue(picture):
  for p in getPixels(picture):
    value = getBlue(p)
    setBlue(p, value * 0.2)



def swapRedAndBlue(picture):
  for p in getPixels(picture):
    redvalue = getBlue(p)
    bluevalue = getRed(p)
    setRed(p, redvalue)
    setBlue(p, bluevalue)
    

file = pickAFile()
myPicture = makePicture(file)
explore(myPicture)
#decreaseRed(myPicture)
#decreaseGreen(myPicture)
#decreaseBlue(myPicture)
swapRedAndBlue(myPicture)
explore(myPicture)


#####