# Part 1
# Relational Operators #
# 1. 19 >= 20 - False
# x = 129 (Variable Assignment)
# 2. x <= 20 - False
# y = 20
# x = 5
# 3. (x * 4) == y - True
# 4. (x * 4) > y - False
# 5. (x * 4) <= y - True (It is equal to)
# 6. True != True - False
# 7. True == True - True
# 8. False == True - False
# x = 5 (Variable Assignment)
# 9. x > 7 - False
########################

# The Keyword 'in' #
# 1. random_word = "Hello" (Variable Assignment)
# 2. "H" in random_word - True
# 3. "h" in random_word - False
# 4. "a" in random_word - False
# 5. shopping_list_prices = [3.24, 5.99, 3.49] (Variable Assignment)
# 6. 5.99 in shopping_list_prices - True
# 7. 3.48 in shopping_list_prices - False
# 8. 3.248 in shopping_list_prices - False
####################
# Part 2

# Example #
# The next two lines execute no matter what!
age = requestInteger("How old are you in years?")
print "You have access to the downstairs area"

#IF Statement
if age >= 21:
  print "As a " + str(age) + " year old, you have access to the upstairs area too!"
  print "And NO, you cannot sneak an underage person upstairs!!!"


print "Have fun!!!"
##########

# 2.2 #
secret_word = "applesauce"
guess = requestString("Please enter in a character from 'a' - 'z'")

if guess in secret_word:
  print "YES! Your character was in the secret word."

print "Thanks for playing"
#######

# 3.1 #
def level_of_access():
  age = requestInteger("How old are you in years?")
  print "You have access to the downstairs area"

  #IF Statement
  if age >= 21:
    print "As a " + str(age) + " year old, you have access to the upstairs area too!"
    print "And NO, you cannot sneak an underage person upstairs!!!"
  
  print "Have fun!!!"

level_of_access()

#######

# 3.2 #

def guess_letter():
  secret_word = "applesauce"
  guess = requestString("Please enter in a character from 'a' - 'z'")

  if guess in secret_word:
    print "YES! Your character was in the secret word."

print "Thanks for playing"

guess_letter()
#######