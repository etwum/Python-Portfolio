print("Welcome to the Calculator\n")

#The program will ask the user to input two numbers
#The program will then perform multiplication, addition and subtraction
fltNumber1 = float(input("Please enter your first number "))  #user input1
fltNumber2 = float(input("Please enter your second number "))  #user input2

fltMultiplication = fltNumber1 * fltNumber2   #performs multiplication 
fltAddition = fltNumber1 + fltNumber2         #performs addition 
fltSubtraction = fltNumber1 - fltNumber2       #performs subtraction 
fltDivision = (fltNumber1)/fltNumber2           #performs division

#prints the results
print("\n\nYour numbers multiplied equal: ", fltMultiplication)
print("Your numbers added together equal: ", fltAddition)
print("The difference between your first number and second number equals: ", fltSubtraction)
print("Your first number divided by the second number equals: ", fltDivision)

input("\nPress enter to continue...")
