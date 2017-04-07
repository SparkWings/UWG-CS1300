def findMax(file):
  opened_file = open(file, "rt")
  lines = opened_file.readlines()
  opened_file.close() 
  len_lines_file = len(lines)
  lines = lines[6:len_lines_file]
  parts = lines[0].split(",")
  max_population = int(parts[7])
  
  for line in lines:  
    parts = line.split(",")
    if int(parts[7]) > max_population:
    
      max_population = int(parts[7])
      state_name = str(parts[4])
 
  print state_name + ' has the maximum population with ' + str(max_population) + ' people.'
def findMin(file):
  opened_file = open(file, "rt")
  lines = opened_file.readlines()
  opened_file.close() 
  len_lines_file = len(lines)
  lines = lines[6:len_lines_file]
  parts = lines[0].split(",")
  min_population = int(parts[7])
  
  for line in lines:  
    parts = line.split(",")
    if int(parts[7]) < min_population:
    
      min_population = int(parts[7])
      state_name = str(parts[4])
      
 
  print state_name + ' has the minimum population with ' + str(min_population) + ' people.'

def findAveragePopulation(file):
  opened_file = open(file, "rt")
  lines = opened_file.readlines()
  opened_file.close() 
  len_lines_file = len(lines)
  lines = lines[6:len_lines_file]
  parts = lines[0].split(",")
  population_total = 0
  
  for line in lines:  
    parts = line.split(",") 
    population_total = population_total + int(parts[7])
    
  population_average = (population_total / 52)
  
  print "The average population of the 50 United States and 2 territories is:", population_average

def findAveragePopulation_statesOnlyChallenge(file):
  opened_file = open(file, "rt")
  lines = opened_file.readlines()
  opened_file.close() 
  len_lines_file = len(lines)
  lines = lines[6:len_lines_file]
  parts = lines[0].split(",")
  population_total = 0
  
  for line in lines:  
    parts = line.split(",")
    
    if parts[4] != "District of Columbia" or parts[4] != "Puerto Rico":   
      population_total = population_total + int(parts[7])
    
  population_average = (population_total / 50)
  
  print "The average population of the 50 United States is:", population_average

file = pickAFile()
  
findMax(file)
findMin(file)
findAveragePopulation(file)
findAveragePopulation_statesOnlyChallenge(file)