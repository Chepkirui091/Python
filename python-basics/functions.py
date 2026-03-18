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