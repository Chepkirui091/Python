# Functions in Python
# Functions are reusable blocks of code

# Simple function
def greet():
    print("Hello! Welcome to Python functions.")

greet()

# Function with parameters
def greet_person(name):
    print(f"Hello, {name}!")

greet_person("Alice")
greet_person("Bob")

# Function with return value
def add_numbers(a, b):
    return a + b

result = add_numbers(5, 3)
print(f"5 + 3 = {result}")

# Function with default parameter
def power(base, exponent=2):
    return base ** exponent

print(f"2^3 = {power(2, 3)}")
print(f"5^2 = {power(5)}")  # Uses default exponent=2

#Python *args and **kwargs (allows functions to accept unknown number of arguments)
def my_functin(*kids):
    print("The youngest child is " + kids[2])
my_functin("Emil", "Tobias", "Linus") 
# *args parameter allows a function to accept any number of positional arguments, which are then accessible as a tuple within the function. In this example, the function my_function takes a variable number of arguments (kids) and prints the third one (Linus). Inside a function args becomes a tuple containing all the passed arguments. You can access the individual arguments using indexing, as shown in the example where kids[2] retrieves the third argument.
def my_function(greeting, *names):
    for name in names:
        print(f"{greeting}, {name}!")
my_function("Hello", "Alice", "Bob", "Charlie")
# In this example, the function my_function takes a greeting and a variable number of names.

# keyword arguments(kwargs) allow you to pass a variable number of keyword arguments to a function. These arguments are accessible as a dictionary within the function. Here's an example:
def my_function(**kid):
    print("His last name is " + kid["lname"])
my_function(fname = "Tobias", lname = "Kibet")

#combining *args and **kwargs
#The order must be: (parameters, *args, **kwargs)
def my_function(title, *args, **kwargs):
    print(f"Title: {title}")
    print("Positional arguments:", args)
    print("Keyword arguments:", kwargs)
    
my_function("User Info", "Alice", "Bob", age=30, city="New York")