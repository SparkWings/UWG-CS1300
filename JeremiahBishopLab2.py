# Part 1 - Data type operations

#1. The output from "print 3/5" is 0 because 3 divided by 5 is less than 1, and an Integer can only represent a whole number value
print 3/5

#2. The output from "print 3.0/5" is 0.6 because the program reads the numbers in the expression as a float, which can return decimal values.
print 3.0/5

#3. The output from the expression is "-38", because the program reads the expression in PEMDAS order -- meaning "5*9" is calculated first, then the other numbers are added/subtracted accordingly.
print 4 - 5 * 9 + 3

#4. The output from the expression is "-6", because the program reads the parenthesis before any other part of the expression (PEMDAS), then calculates the multiplication/addition.
print (4 - 5) * 9 + 3

#5. The output is "Hola,Como estas?" because you are conjoining two Strings without a space.
print "Hola," + "Como estas?"

#6. The error output is "cannot concatenate 'str' and 'int' objects", because here you are trying to add a String an an integer
#print "Hola," + 5

#7. The output is "Hola," 5x, because you are telling the program to print it 5 times.
print "Hola," * 5

#8. The output is "Hola,Como estas?", because you are conjoining two Strings.
print "Hola," + "Como estas?"

#9. The output is "Hola,5" because you are conjoining the String "Hola" and the [String] "5".
print "Hola," + "5"

#10. The error output is "can't multiply sequence by non-int of type 'str'", because you can't multiply a String by another String.
#print "Hola," * "5"

#######################################

#Part 2 - Variables and Function Calls

#1. The output from the code is "The product is: -18", because "a * b" is -18, the value of "x"
a = -3
b = 6
x = a * b
print "The product is:", x

#2. The output is -66, because above the variable a is assigned -3; meaning that "-3 * 22" is -66.
b = a
a = 22
x = a * b
print "The new product is:", x

#3. The output is 7, because "6 - -3/3" is 7; abs() returns the absolute value of an Integer
#a = -3
#b = 6
#c = abs(a)
#x = b - a/c
#print "The final output is:", x

#4. By changing the variable values, we can manipulate the "final output" to be 3.
a = 3 
b = 4
c = abs(a) 
x = b - a/c 
print "The final output is:", x 

#5. The output is the name entered (Eg. "Jeremy"), because you are assigning the variable name to the input of the user; requestString requests a String from the user.
name = "Ana"
name = requestString("Please type in your name:")
print name

#6. The output is "GeorgeWashington", because we are conjoining two strings.
#first_name = "George"
#last_name = "Washington"
#print first_name + last_name

#7. Now the output is "George Washington, because you added a space.
first_name = "George "
last_name = "Washington"
print first_name + last_name

#######################################

#Part 3 - Syntax Errors

#1. The program does not run correctly because we did not add a closing parenthesis. "You may have not have as many closing parentheses as opening parentheses, left the ending quote off of a string, or tried to use a Jython keyword (if, def, etc...) as a function."

#2. The program does not run correctly and gives the same error because we did not add as many closing quotations as we had opening quotations.

#3 The program does not run because "requestString() = name" is not valid Jython.

#4 The program does not run because there is no such function as "requeststring", only "requestString"; Errir: "A local or global name could not be found. You need to define the function or variable before you try to use it in any way."
# Error is found on page: ? [I don't have the book yet :( ]

#5. The statement "x = 7 / " will produce an error because there is no integer after "7" to divide by, meaning there is a syntax error.