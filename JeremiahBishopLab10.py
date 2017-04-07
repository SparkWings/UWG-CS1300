def translateString(string):
  
  newString = ""
  string_len = len(string)
  
  for index in range(string_len):
    letter = string[index]
    
    if(letter.isdigit()):
      letter = " [digit]"
    if(index % 2 == 0):
      letter = letter.capitalize()
      
    newString = newString + letter
  print newString
  
  
def reverseString(string):
  newString = ""
  
  for index in reversed(string):
    newString = newString + index
  
  print newString

def findPopulation(state):
  file = open(pickAFile(), "rt")
  lines = file.readlines()
  file.close
  
  for line in lines:
    parts = line.split(",")
    if parts[4].capitalize() == state:
      return int(parts[5])
  return -1
      
def percentageGenders(string):
  gen_len = len(string)
  
  num_f = 0.0
  num_m = 0.0
  
  for letter in string:
    if letter == "F":
      print num_f++
    
    if letter == "M":
      print num_m++
      
  avg_m = num_m / gen_len
  avg_f = num_f / gen_len
  print avg_m                    
  print avg_f
string_one = requestString("Please input a sentence")
string_two = requestString("Please input another sentence")

translateString(string_one)
reverseString(string_two)
myint = findPopulation("GeoRgia")
print myint

percentageGenders("MFMFMFMF")