# Variables in Python
# Variables are used to store data values
#Pyhton variables are reserved memory locations used to store values with python programming language. Unlike other programming languages, Python has no command for declaring a variable. A variable is created the moment you first assign a value to it. The equal sign (=) is used to assign values to variables..

# String variable
name = "Alice"
print("Name:", name)

# Integer variable
age = 25
print("Age:", age)

# Float variable
height = 5.6
print("Height:", height)

# Boolean variable
is_student = True
print("Is student:", is_student)

# You can change variable values
age = 26
print("New age:", age)

#You can delete a variable using the del keyword
counter = 100
print (counter)

# del counter
print (counter) 
# This will raise a NameError because counter has been deleted

# You can get the data tye of a variable using the type() function
print("Type of name:", type(name))
print("Type of age:", type(age))    

#You can also assign multiple variables at once
x, y, z = 1, 2.5, "Hello"
print("x:", x)
print("y:", y)
print("z:", z)

# You can also assign the same value to multiple variables
a = b = c = 10
print("a:", a)
print("b:", b)
print("c:", c)

#You can specify the data type of a variable using type hints (optional in Python)
x = str(10)    # x will be '10'
y = int(10)    # y will be 10 
z = float(10)  # z will be 10.0

print( "x =", x )
print( "y =", y )
print( "z =", z )

'''
#Naming rules for variables in Python:
A variable name must start with a letter or the underscore character
A variable name cannot start with a number or any special character like $, (, * % etc.
A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
Python variable names are case-sensitive which means Name and NAME are two different variables in Python.
Python reserved keywords cannot be used naming the variable.
If the name of variable contains multiple words, we should use these naming patterns −

Camel case − First letter is a lowercase, but first letter of each subsequent word is in uppercase. For example: kmPerHour, pricePerLitre

Pascal case − First letter of each word is in uppercase. For example: KmPerHour, PricePerLitre

Snake case − Use single underscore (_) character to separate words. For example: km_per_hour, price_per_litre
'''

#You can also use variables to store the result of expressions
a = 10
b = 5   
sum = a + b
print("Sum:", sum)

#You can also use variables in f-strings for formatted output
name = "Alice"
age = 30
print(f"{name} is {age} years old.")

#You can also use variables in string concatenation
greeting = "Hello, " + name + "!"
print(greeting)

#Python Local Variables are defined inside a function. We can not access variable outside the function.
