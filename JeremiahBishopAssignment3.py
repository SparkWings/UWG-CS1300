###################Part 1#######################
#This method takes in a requested miles integer (or float) and converts it to kilometers
def mileageConverter():
  distance_miles = requestInteger("What is the distance in miles?")
  distance_kilos = (distance_miles * 1.6)

  print "The distance in kilometers is:", distance_kilos

################################################

#This method requests 2 integers, base and height size, to calculate the appropriate area of a triangle.
def calculateAreaTriangle():
  tri_height = requestInteger("What is the height of the triangle?")
  tri_base = requestInteger("What is the base size of the triangle?")
  
  tri_area = 0.5 * (tri_base * tri_height)
  print "A triangle with a base of", tri_base,"and a height of",tri_height,"has an area of",tri_area 
  
###################Part 2########################

#This method calculates shipping cost by pound.
def calculateShippingCosts(item_weight, item_cost_per_lb):
  total_cost = item_weight * item_cost_per_lb
  print "A package weighing",item_weight,"pounds with a per pound shipping cost of $",item_cost_per_lb,"totals $",total_cost,"."

################################################

#This method estimates the amount of time it will take to travel between 2 points.
def travelTimeCalculator(speed, distance_miles, departure_time):
  travel_time = distance_miles / speed
  arrival_time = departure_time + travel_time
  
  print "Leaving at ",departure_time," and traveling at an average of ",speed,"mph, you should arrive at your destination at approximately:", arrival_time

################################################


#mileageConverter()
#calculateAreaTriangle()
#calculateShippingCosts(50, 7.33)
travelTimeCalculator(70, 46.6, 11.75)
