## 1.1 ##
#This function takes all the RGB values of an image and decreases them by an interval of 30
def decreaseRGB(picture):
  for aPixel in getPixels(picture):
    blue_val = getBlue(aPixel) - 30
    red_val = getRed(aPixel) - 30
    green_val = getGreen(aPixel) - 30
    setBlue(aPixel, blue_val)
    setRed(aPixel, red_val)
    setGreen(aPixel, green_val)
#########
## 1.2 ##
# This function takes any blue pixel values greater than 128 and sets them to 0
# Giving the image a yellow-ish tint.
def affectOnlyBlue(picture):
  for aPixel in getPixels(picture):
    blue_val = getBlue(aPixel)
    red_val = getRed(aPixel)
    green_val = getGreen(aPixel)

    if blue_val > 128:
      blue_val = 0 
      
    setBlue(aPixel, blue_val)
    setRed(aPixel, red_val)
    setGreen(aPixel, green_val)

#################################
## 1.3 ##
def affectAllColors(picture):
  for aPixel in getPixels(picture):
    blue_val = getBlue(aPixel)
    red_val = getRed(aPixel)
    green_val = getGreen(aPixel)

    blue_val = 0
      
    red_val = 30
      
    green_val = 0
      
    setBlue(aPixel, blue_val)
    setRed(aPixel, red_val)
    setGreen(aPixel, green_val)
####################
## 1.4 ##
# The next two lines execute no matter what!
age = requestInteger("How old are you in years?")

#IF Statement
if age >= 21:
  print "As a " + str(age) + " year old, you have access to the upstairs area too!"
  print "And NO, you cannot sneak an underage person upstairs!!!"

else:
  print "As a " + str(age) + " year old, you are considered underage"
  print "You have access only to the downstairs area." 

print "Have fun!!!"
##########
## 2.2 ##
def affectOnlyBlue_2(picture):
  for aPixel in getPixels(picture):
    blue_val = getBlue(aPixel)
    red_val = getRed(aPixel)
    green_val = getGreen(aPixel)
    if blue_val > 128: 
      blue_val = 255 
    else: 
      blue_val = 0
      
    if red_val > 128: 
      red_val = 255 
    else: 
      red_val = 0
      
    if green_val > 128: 
      green_val = 255 
    else: 
      green_val = 0
      
    setBlue(aPixel, blue_val)
    setRed(aPixel, red_val)
    setGreen(aPixel, green_val)
#####################
## 2.3 ##
def makeBlackAndWhite(picture):
  for aPixel in getPixels(picture):
    blue_val = getBlue(aPixel)
    red_val = getRed(aPixel)
    green_val = getGreen(aPixel)
    
    average = (blue_val + red_val + green_val) / 3
    
    if average > 128:
      setBlue(aPixel, average)
      setRed(aPixel, average)
      setGreen(aPixel, average)
    
    else:
      setBlue(aPixel, 0)
      setRed(aPixel, 0)
      setGreen(aPixel, 0)

file = pickAFile() 
myPicture = makePicture(file)
explore(myPicture) 
#decreaseRGB(myPicture)
#affectOnlyBlue(myPicture) 
affectAllColors(myPicture)
#affectOnlyBlue_2(myPicture)
#makeBlackAndWhite(myPicture)
explore(myPicture) 
