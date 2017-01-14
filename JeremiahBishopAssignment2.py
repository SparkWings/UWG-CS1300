#Part 1 - Play with Data Types

#1.
print "Bon " + "Jour"

#2. 
a = 5
b = a
print a * b

#3.
print "Hi There!" * 5

#4. 
a = 5.0
b = 2
print a / b

#5.
print "4"+"5"

##############################

#Part 2 - Writing a correct program

#1. The Honda Oddessy traveled 334 miles and just filled up with 15.8 gallons of gas. What is the miles per gallon for this trip?
#Answer: The multiplication symbol in the statement "trip_mpg = miles_traveled * gallons_of_gas" should have been changed to division, to properly fit the MPG formula.
miles_traveled = 334
gallons_of_gas = 15.8
trip_mpg = miles_traveled / gallons_of_gas
print trip_mpg

#2. Your 3 year niece is so excited to see you that she runs up to you calling your name 5 times.
#Answer: The statement "requestString() = name" should be flipped to "name = requestString()"
name = requestString("What is your name?")
name_repeated = name * 5
print "Yeeeeaaaahhh " + name_repeated + "!!!!"

#3. The program should ask you your age and calculate it in seconds.
#Answer: The division symbol between the two 60's should be changed to a multiplication sign.
age = requestInteger("What is your age in years?")
seconds = age * 365 * 24 * 60 * 60
print "Did you know that you are over", seconds, "seconds old."

#4.The moon has one-sixth the gravitational pull of earth and the sun has a gravitational force of approximately 27.1 times stronger than here on earth.
#Write a program that will print the person's weight on the moon and on the sun on two separate lines.
#Answer: The last statement should pass the "sun_weight" variable in instead of the "moon_weight" variable.
weight = requestInteger("What is your weight in pounds?")
moon_weight = weight / 6
sun_weight = weight * 27.1
print "Did you know that you would weigh", moon_weight, "pounds on the moon."
print "Did you know that you would weigh", sun_weight, "pounds on the sun...but not for very long ;-)"

#The program should ask the user to enter two of his/her favorite foods. The program should then print out the name of a new food by joining the original food names together with a space in between.
#Solution: The hyphen in the "print" statement should be replaced with a space"
favFood1 = requestString("What is your first favorite food?")
favFood2 = requestString("What is your second favorite food?")
newFavFood = favFood1 + " " + favFood2
print newFavFood 

##################################

### CHALLENGE ###
car_base_price = requestInteger("What is the base price of your car?")
ad_velorem = car_base_price * 0.075
license_fee = 25
dealer_prep_fee = 325
destination_fee = 800
total = car_base_price + ad_velorem + license_fee + dealer_prep_fee + destination_fee
print "----- Invoice (Your New Car) -----"
print "Original Cost: $", car_base_price
print "Tax Fees: $", ad_velorem
print "Licence Fee: $", license_fee
print "Dealer Prep Fee: $", dealer_prep_fee
print "Destination Charge: $", destination_fee
print "Total: $", total
print "----------------------------------"
