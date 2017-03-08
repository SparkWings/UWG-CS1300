def overlay_image(picture):
  all_pixels = getPixels(picture)
  len_all_pixs = len(all_pixels)
  
  half_len_pix = (len_all_pixs / 2)
  
  for index in range(half_len_pix):
    the_pixel = all_pixels[index]
    
    red_val = getRed(the_pixel)
    avg = (red_val + 255) / 2
    
    setRed(the_pixel, avg)
    
  for index in range(half_len_pix, (len_all_pixs - 1)):
    the_pixel = all_pixels[index]
    blue_val = getBlue(the_pixel)
    avg = (blue_val + 255) / 2
    
    setBlue(the_pixel, avg)
    
def decreaseRed_leftHalf(picture, percentage):
  all_pixels = getPixels(picture)
  len_all_pixs = len(all_pixels)

  width_picture = getWidth(picture)
  half_width_pict = width_picture / 2
  
  
  for index in range(len_all_pixs):
    the_pixel = all_pixels[index]
    x = getX(the_pixel)
    
    if x < half_width_pict:
      red_val = getRed(the_pixel)
      setRed(the_pixel, red_val * (1 - percentage))
      

def decreaseBlue_rightHalf(picture, percentage):
  all_pixels = getPixels(picture)
  len_all_pixs = len(all_pixels)

  width_picture = getWidth(picture)
  half_width_pict = width_picture / 2
  
  
  for index in range(len_all_pixs):
    the_pixel = all_pixels[index]
    x = getX(the_pixel)
    
    if x > half_width_pict:
      blue_val = getBlue(the_pixel)
      setBlue(the_pixel, blue_val * (1 - percentage))
      
      
def overlay_rwb(picture, percentage):
  all_pixels = getPixels(picture)
  len_all_pixs = len(all_pixels)

  width_picture = getWidth(picture)
  
  first_section = range(0, (width_picture * 0.3))
  second_section = range(width_picture * 0.3, width_picture * 0.7)
  third_section = range(width_picture * 0.7, width_picture * 1.0)
  
  for index in range(len_all_pixs):
    the_pixel = all_pixels[index]
    x = getX(the_pixel)
    
    if x in first_section: #Red
      setRed(the_pixel, getRed(the_pixel) * (1 + percentage))
      
    if x in second_section: #White          
      setRed(the_pixel, getRed(the_pixel) + (percentage * 2))
      setGreen(the_pixel, getGreen(the_pixel) + (percentage * 2))
      setBlue(the_pixel, getBlue(the_pixel) + (percentage * 2))
      
    if x in third_section: #Blue
      setBlue(the_pixel, getBlue(the_pixel) * (1 + percentage))

    

    
file = pickAFile()
myPicture = makePicture(file)
explore(myPicture)
#overlay_image(myPicture)
#decreaseRed_leftHalf(myPicture, 50)
#decreaseBlue_rightHalf(myPicture, 50)
overlay_rwb(myPicture, 50)
explore(myPicture)