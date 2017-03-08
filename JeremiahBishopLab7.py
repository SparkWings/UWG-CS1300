#Warmup: print phrase[0] returns the value "M".
# Part 1 #
phrase = "Men's Gymnastics Rocks!"
length_of_phrase = len(phrase)

print phrase[17]
print phrase[length_of_phrase - 6]
print phrase[0]
print phrase[-1]
print phrase[2]

# Part 2 #
phrase = "Jeremiah Bishop"
length_of_phrase = len(phrase)

print length_of_phrase
print range(length_of_phrase)

# 2.2 #
def wordTriangle_index(collection):
  word = ""
  
  length_of_string = len(collection)
  
  for index in range(length_of_string):
    word = word + collection[index]
    print word
  
  print "Finished."

# 2.3 #
def modifiedWordTriangle_index(collection):
  word = ""
  
  length_of_string = len(collection)
  
  for index in range(length_of_string):
    word = collection[index] + word + collection[index]
    print word
  
  print "Finished."

wordTriangle_index("Programming")

modifiedWordTriangle_index("Programming")

# Part 3 #
roster = ["Madison", "Howard", "Matthew", "Darius", "Eliza"]
length_of_roster = len(roster)

print length_of_roster #Prints 5
print roster[0] #Prints Madison
print roster[-1] #Prints Eliza

print roster[2]
print roster[-3]
print roster[length_of_roster - 1]
print roster[4]

def print_roster(the_roster):
  length_of_roster = len(the_roster)
  
  for index in range(length_of_roster):
    student_number = index + 1
    print "Student #" + str(student_number) + ":", the_roster[index]
  

print_roster(roster)

# 3.3 #
def average_grades(list_grades):
  len_grades = len(list_grades)
  
  currentTotal = 0
  
  for index in range(len_grades):
    currentTotal = currentTotal + list_grades[index]
    
  avg_grades = (currentTotal / len_grades)
  print "The average of the inputted", str(len_grades), "is", avg_grades
  
grades_section1 = [89.7, 90.3, 56, 87, 69.9]
grades_section2 = [77.4, 55.3, 56, 87, 55.3, 78, 91, 69.9, 99, 78.9, 60, 95.3]

average_grades(grades_section1)
average_grades(grades_section2)