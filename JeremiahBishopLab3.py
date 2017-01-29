### Part 1 - Review###

user_char = requestString("Please enter a character.")
number_repeat = requestInteger("Please enter how many times you would like to repeat the character.")
number_string = str(number_repeat)

print "The user wants to print the character", user_char, number_repeat, "times."
print user_char * number_repeat
######################

# Part 2a - Define Functions without parameters #

#function that loads and shows the user a picture.
def exploreMyPicture():
  print "Please select an IMAGE FILE to display."
  
  file = pickAFile()
  picture = makePicture(file)
  
  explore(picture)

def ageCalculator():
  birthYear = requestNumber("What is your birthyear? (ex. 1998)")
  currentYear = 2017
  
  age = currentYear - birthYear
  
  userName = requestString("What is your name?")
  
  print "Hi", userName, ", you are", str(age), "years old."

exploreMyPicture()
ageCalculator() 
#############################################

# Part 2b - Define Functions with parameters #

#Function to print information provided about the user
def aboutMe(first_name, last_name, graduating_highschool, favorite_movie):
  print "Full Name:" + first_name + " " + last_name
  
  print "Graduating Highschool:", graduating_highschool
  
  print "Favorite Movie:", favorite_movie

#Function to calculatehow much money is in the tip jar
def tipJar(quarters, dimes, nickels, pennies):
  quarter_value = 0.25
  dime_value = 0.1
  nickel_value = 0.05
  penny_value = 0.01
  
  quartersToDollars = quarter_value * quarters
  dimesToDollars = dime_value * dimes
  nickelsToDollars = nickel_value * nickels
  penniesToDollars = penny_value * pennies
  
  total = quartersToDollars + dimesToDollars + nickelsToDollars + penniesToDollars
  
  print "The tip jar contains:"
  print str(quarters) + " Quarters"
  print str(dimes) + " Dimes"
  print str(nickels) + " Nickels"
  print str(pennies) + " Pennies"
  print "This totals $", total

aboutMe("Jeremy", "Bishop", "Heard County High School", "Suicide Squad")
tipJar(5, 0, 0, 0)

############################################

