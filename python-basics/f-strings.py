# f strings, also known as formatted string literals, are a way to embed expressions inside string literals, using a minimal syntax. They were introduced in Python 3.6 and provide a more readable and concise way to format strings compared to older methods like str.format() or the % operator.
# To create an f-string, you prefix the string with the letter 'f' or 'F' and include expressions inside curly braces {}. The expressions are evaluated at runtime and their values are inserted into the string. Here are some examples of using f-strings in Python:  
name = "Alice"
age = 30
# Basic usage of f-strings
greeting = f"Hello, {name}! You are {age} years old."   
print(greeting)  # Output: Hello, Alice! You are 30 years old.
# You can also include expressions inside the curly braces
result = f"The sum of 5 and 10 is {5 + 10}."
print(result)  # Output: The sum of 5 and 10 is 15. 
# F-strings also support formatting options for numbers, dates, and other types. For example:
pi = 3.14159
formatted_pi = f"Pi is approximately {pi:.2f}."
print(formatted_pi)  # Output: Pi is approximately 3.14.    
from datetime import datetime
now = datetime.now()
formatted_date = f"Today is {now:%Y-%m-%d}."
print(formatted_date)  # Output: Date today is 2024-06-01. (or the current date when you run the code)
# You can also use f-strings to call functions and access object attributes
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

person = Person("Bob", 25)
greeting = f"Hello, {person.name}! You are {person.age} years old."
print(greeting)  # Output: Hello, Bob! You are 25 years old.    
# F-strings provide a powerful and flexible way to format strings in Python, making it easier to create dynamic and readable output. They are generally preferred over older string formatting methods for their simplicity and improved readability.

# F-strings also support the use of expressions and can be used to format numbers, dates, and other types. For example:
number = 1234.56789
formatted_number = f"The number is {number:.2f}."
print(formatted_number)  # Output: The number is 1234.57.

#the old way of formatting strings using the % operator
name = "Alice"
age = 30
greeting = "Hello, %s! You are %d years old." % (name, age)
print(greeting)  # Output: Hello, Alice! You are 30 years old.