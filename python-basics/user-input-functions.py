# There are two built in functions to read inputs from keyboard.

#The input() functions 
'''
When the interpreter encounters input() function, it waits for the user to enter data from the standard input stream (keyboard) till the Enter key is pressed. The sequence of characters may be stored in a string variable for further use.
The input() function can also take an optional argument, which is a string that will be displayed as a prompt to the user before waiting for input. For example:
name = input("Please enter your name: ")
'''

name = input("Please enter your name: ")
print("Hello, " + name + "!")

# The raw_input() function
'''
In Python 2.x, there was a function called raw_input() that served a similar purpose to input() in Python 3.x. The raw_input() function reads a line of input from the user and returns it as a string. However, in Python 3.x, the raw_input() function has been removed, and the input() function now behaves like raw_input() did in Python 2.x. Therefore, if you are using Python 3.x, you should use the input() function to read user input.
'''
# city = raw_input("Please enter your city: ")
# print("You live in " + city + ".")

'''
    city = raw_input("Please enter your city: ")
           ^^^^^^^^^
NameError: name 'raw_input' is not defined '''


#Since input() function returns a string, if you want to read a number from the user, you need to convert the input string to the appropriate numeric type (e.g., int or float) using the int() or float() functions. For example:
age = int(input("Please enter your age: "))
print("You are " + str(age) + " years old.")