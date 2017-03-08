# Part 1 #

myPicture = makeEmptyPicture(3, 3)
colors = [red, green, blue, white, black, yellow, orange, pink, cyan]
all_pixels = getPixels(myPicture)
len_all_pixs = len(all_pixels) 

for index in range(len_all_pixs):
  a_color = colors[index]
  my_pixel = all_pixels[index]
  setColor(my_pixel, a_color)

for index in range(len_all_pixs):
  print all_pixels[index]


## 1.2 ##

def decreaseRed(picture, percentage):
  all_pixels = getPixels(picture)
  len_all_pixs = len(all_pixels)
  
  for index in range(len_all_pixs):
    the_pixel = all_pixels[index]
    
    red_val = getRed(the_pixel)
    
    setRed(the_pixel, red_val * (1 - percentage))
    
## 1.3 ##
    
def decreaseBlue(picture, percentage):
  all_pixels = getPixels(picture)
  len_all_pixs = len(all_pixels)
  
  for index in range(len_all_pixs):
    the_pixel = all_pixels[index]
    
    blue_val = getBlue(the_pixel)
    
    setBlue(the_pixel, blue_val * (1 - percentage))
    
def decreaseGreen(picture, percentage):
  all_pixels = getPixels(picture)
  len_all_pixs = len(all_pixels)
  
  for index in range(len_all_pixs):
    the_pixel = all_pixels[index]
    
    green_val = getGreen(the_pixel)
    
    setGreen(the_pixel, green_val * (1 - percentage))
  

## 2.1 ##

def decreaseRed_topHalf(picture, percentage):
  all_pixels = getPixels(picture)
  len_all_pixs = len(all_pixels)
  
  half_len_pix = (len_all_pixs / 2)
  
  for index in range(half_len_pix):
    the_pixel = all_pixels[index]
    
    red_val = getRed(the_pixel)
    
    setRed(the_pixel, red_val * (1 - percentage))

## 2.2 ##

def decreaseGreen_bottomHalf(picture, percentage):
  all_pixels = getPixels(picture)
  len_all_pixs = len(all_pixels)
  
  half_len_pix = (len_all_pixs / 2)
  
  for index in range(half_len_pix, (len_all_pixs - 1)):
    the_pixel = all_pixels[index]
    
    green_val = getGreen(the_pixel)
    
    setGreen(the_pixel, green_val * (1 - percentage))

## 3.0 ##

def stripeImage(picture):
  all_pixels = getPixels(picture)
  len_all_pixs = len(all_pixels)
  
  half_len_pix = (len_all_pixs / 2)
  
  for index in range(0, (len_all_pixs - 1), 5):
    the_pixel = all_pixels[index]
    
    setBlue(the_pixel, 255)
                                                                        
file = pickAFile()
myPicture = makePicture(file)
explore(myPicture)
#decreaseRed(myPicture, 50)
#decreaseGreen(myPicture, 50)
#decreaseBlue(myPicture, 50)
#decreaseRed_topHalf(myPicture, 50)
#decreaseGreen_bottomHalf(myPicture, 50)
stripeImage(myPicture)
explore(myPicture)