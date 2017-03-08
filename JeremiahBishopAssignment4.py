## 1.1 ##
print range(0, 10)
print range(4, 21)
print range(2, 22, 2)
print range(31, 9, -2)
#########

## 1.2 ##
def blastoff():
  for i in range(10, -1, -1):
    print i
    
  print "Blastoff!!!"


blastoff()
##########

## 1.3 ##

#This method creates a square of characters and prints it to the user.
def textsquare(character, numTimes):
  for i in range(numTimes, 0, -1):
    print character*numTimes
    
    
textsquare("#", 5)
#########

## 1.4 ##

#This method adds all terms in a range of 1 to x and prints them for the user.
def sum_sequence(rangeTop):
  sum_of_sequence = 0
  
  for i in range(1, rangeTop + 1, 1):
    sum_of_sequence = sum_of_sequence + i
  
  print "The sum of the first", rangeTop, "integers is", sum_of_sequence, "."

sum_sequence(35)
#########