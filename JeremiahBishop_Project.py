#Successfully completed Part 1 of the final project.
#Successfully completed Part 2 of the final project.
#Successfully completed Part 3 of the final project.

#Part 1 -- Statistics
#Overlord Function -- Takes selected file input (in csv format) and calculates the user's grades; runs all other functions
def calculateGrade():
  gradeFile = pickAFile()
  
  #Part 1 Functions
  getHighestGrade(gradeFile)
  getLowestGrade(gradeFile)
  getUnweightedFinalAverage(gradeFile)
  getNumGradesAbovePassing(gradeFile)
  getPassingGradePercentage(gradeFile)
  
  #Part 2 Funtcions
  calculateAverages(gradeFile)
  
  #Part 3 Functions
  countGrades(gradeFile)
  

#Prints the highest grade from the CSV file
def getHighestGrade(file):
  opened_file = open(file, "rt")
  lines = opened_file.readlines()
  opened_file.close() 
  len_lines_file = len(lines)
  lines = lines[1:len_lines_file]
  parts = lines[0].split(",")
  
  max_grade = 0.0
  
  for line in lines:  
    parts = line.split(",")
    current_grade = int(parts[2])
    
    if current_grade > max_grade:
      max_grade = current_grade
      
  printNow("Highest Grade: " + str(max_grade) + "%")

#Prints the lowest grade from the CSV file
def getLowestGrade(file):
  opened_file = open(file, "rt")
  lines = opened_file.readlines()
  opened_file.close() 
  len_lines_file = len(lines)
  lines = lines[1:len_lines_file]
  parts = lines[0].split(",")
  
  min_grade = parts[2]
  
  for line in lines:  
    parts = line.split(",")
    current_grade = int(parts[2])
    
    if current_grade < min_grade:
      min_grade = current_grade
      
  printNow("Lowest Grade: " + str(min_grade) + "%")

#Prints an average using the formula (sum of grades / number of grades)
def getUnweightedFinalAverage(file):
  gradeFile = open(file, "rt")
  lines = gradeFile.readlines()
  gradeFile.close() 
  len_lines_file = len(lines)
  lines = lines[1:len_lines_file]
  parts = lines[0].split(",")
  
  grade_total = 0.0
  
  for line in lines:  
    parts = line.split(",")
    current_grade = int(parts[2])    
    grade_total = (grade_total + current_grade)
 
  grade_average = (grade_total / (len_lines_file - 1))
  printNow("Final (Unweighted) Average: " + str(grade_average) + "%")

#Prints the number of grades above 60%
def getNumGradesAbovePassing(file):
  gradeFile = open(file, "rt")
  lines = gradeFile.readlines()
  gradeFile.close() 
  len_lines_file = len(lines)
  lines = lines[1:len_lines_file]
  parts = lines[0].split(",")
  
  passing_grades = 0.0
  
  for line in lines:  
    parts = line.split(",")
    current_grade = int(parts[2])
    
    if current_grade > 60.0:
      passing_grades = passing_grades + 1
      
  printNow("Passing Grades (Grades > 60%): " + str(passing_grades))
    
#Prints the percentage of user grades above 60%
def getPassingGradePercentage(file):
  gradeFile = open(file, "rt")
  lines = gradeFile.readlines()
  gradeFile.close() 
  len_lines_file = len(lines)
  lines = lines[1:len_lines_file]
  parts = lines[0].split(",")
  
  total_grades = len_lines_file - 1
  passing_grades = 0.0
  
  for line in lines:  
    parts = line.split(",")
    current_grade = int(parts[2])
    
    if current_grade > 60.0:
      passing_grades = passing_grades + 1
    
  passing_percentage = ((passing_grades / total_grades) * 100)
  
  printNow("Passing Grade Percentage: " + str(passing_percentage) + "%")


#Part 2 -- Data Analysis
# 'Mini' overlord function for Part 2. Creates the format of the printed strings, because all functions of part 2
# return an integer value and do not print anything by themselves.
def calculateAverages(gradeFile):
  
  print "The UNweighted Assignment grade average is: " + str(calculateUnweightedAverage(gradeFile, "assignment") + "%")
  print "The Weighted Assignment grade average is: " + str(calculateWeightedAverage(gradeFile, "assignment") + "%")
  
  print ""
  
  print "The UNweighted Lab grade average is: " + str(calculateUnweightedAverage(gradeFile, "lab") + "%")
  print "The Weighted Lab grade average is: " + str(calculateWeightedAverage(gradeFile, "lab") + "%")
  
  print ""
  
  print "The UNweighted Quiz grade average is: " + str(calculateUnweightedAverage(gradeFile, "quiz") + "%")
  print "The Weighted Quiz grade average is: " + str(calculateWeightedAverage(gradeFile, "quiz") + "%")

  print ""
   
  print "The UNweighted Project grade average is: " + str(calculateUnweightedAverage(gradeFile, "project") + "%")
  print "The Weighted Project grade average is: " + str(calculateWeightedAverage(gradeFile, "project") + "%")
  
  print ""
  
  getUnweightedFinalAverage(gradeFile)
  
#Calculates an unweighted grade average based on the type of grade (i.e Assignment, Project, Lab, Quiz)
def calculateUnweightedAverage(file, gradeType):
  gradeFile = open(file, "rt")
  lines = gradeFile.readlines()
  gradeFile.close() 
  len_lines_file = len(lines)
  lines = lines[1:len_lines_file]
  parts = lines[0].split(",")
  
  grade_total = 0.0
  num_grades = 0.0
  
  for line in lines:  
    parts = line.split(",")
    current_grade = int(parts[2])    
    
    if parts[0] == gradeType:
      grade_total = (grade_total + current_grade)
      num_grades = num_grades + 1
 
  grade_average = (grade_total / num_grades)
  
  return grade_average  

#Calculates a weighted grade average based on the type of grade (i.e Assignment, Project, Lab, Quiz)
#and its corresponding weight
def calculateWeightedAverage(file, gradeType):
  unweighted_average = calculateUnweightedAverage(file, gradeType)
  weight = 0.0
  
  if gradeType == "assignment":
    weight = 0.45
  elif gradeType == "lab":
    weight = 0.2
  elif gradeType == "quiz":
    weight = 0.15
  else:
    weight = 0.2
    
  weighted_average = (unweighted_average * weight)
  
  return weighted_average


#Part 3 -- Grade Representation
#Creates a 'bar graph' of asterisks based on how many grades of each type the user has
def countGrades(gradeFile):
  gradeFile = open(gradeFile, "rt")
  lines = gradeFile.readlines()
  gradeFile.close() 
  len_lines_file = len(lines)
  lines = lines[1:len_lines_file]
  parts = lines[0].split(",")
  
  grades_a = 0
  grades_b = 0
  grades_c = 0
  grades_d = 0
  grades_f = 0
  
  for line in lines:  
    parts = line.split(",")
    current_grade = int(parts[2])    
    
    if current_grade > 89:
      grades_a = grades_a + 1
      
    elif current_grade < 90 and current_grade > 79:
      grades_b = grades_b + 1
      
    elif current_grade < 80 and current_grade > 69:
      grades_c = grades_c + 1
    
    elif current_grade < 70 and current_grade > 59:
      grades_d = grades_d + 1
      
    elif current_grade < 60:
      grades_f = grades_f + 1
      
  
  print "Count A's: " + ('*' * grades_a)
  print "Count B's: " + ('*' * grades_b)
  print "Count C's: " + ('*' * grades_c)
  print "Count D's: " + ('*' * grades_d)
  print "Count F's: " + ('*' * grades_f)
 
   
#Overlord function call
calculateGrade()