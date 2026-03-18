# Data Types in Python
# Python has several built-in data types

# Strings
message = "Hello, Python!"
print("String:", message)
print("Type:", type(message))

# Integers
number = 42
print("Integer:", number)
print("Type:", type(number))

# Floats
pi = 3.14159
print("Float:", pi)
print("Type:", type(pi))

#Complex numbers
#A complex number is made up of two parts - real and imaginary. They are separated by '+' or '-' signs.
complex_number = 2 + 3j
print("Complex number:", complex_number)
print("Type:", type(complex_number))

# Booleans
is_true = True
is_false = False
print("Boolean True:", is_true)
print("Boolean False:", is_false)
print("Type:", type(is_true))

# Lists (collections) doesn't have to be of the same data type unlike arrays in other programming languages
list = [2023, "Python", 3.11, 5+6j, 1.23E-4]
tinylist = [123, 'john']
print("List:", list)
print("Type:", type(list))

print (list)            # Prints complete list
print (list[0])         # Prints first element of the list
print (list[1:3])       # Prints elements starting from 2nd till 3rd 
print (list[2:])        # Prints elements starting from 3rd element
print (tinylist * 2)    # Prints list two times
print (list + tinylist) # Prints concatenated lists

#Tuples (immutable lists) Unlike lists, tuples are immutable, meaning that once they are created, their elements cannot be changed. Tuples are defined using parentheses () instead of square brackets [].
tuple = (2023, "Python", 3.11, 5+6j, 1.23E-4)
print("Tuple:", tuple)
print("Type:", type(tuple))

#Ranges
#A range is a sequence of numbers that is commonly used for looping a specific number of times in for loops. The range() function generates a sequence of numbers based on the specified start, stop, and step values.
'''
start: Integer number to specify starting position, (Its optional, Default: 0)

stop: Integer number to specify ending position (It's mandatory)

step: Integer number to specify increment, (Its optional, Default: 1)
'''
range1 = range(5)          # Generates numbers from 0 to 4
range2 = range(1, 10)      # Generates numbers from 1 to 9
range3 = range(0, 20, 2)  # Generates even numbers from 0 to 18
print("Range 1:", (range1))
print("Range 2:", (range2)) 
print("Range 3:", (range3))

for i in range(5):
    print("Loop iteration:", i) 
    
#Binary data types
#Bytes: A bytes object is an immutable sequence of bytes, which are 8-bit values. They are commonly used for handling binary data, such as files or network communication.

# Using bytes() function to create bytes
b1 = bytes([65, 66, 67, 68, 69])  
print(b1) # Output: b'ABCDE'

#Using prefix b to create bytes
b2 = b"Hello, World!"
print(b2) # Output: b'Hello, World!'    

#Bytearray: A bytearray is a mutable sequence of bytes. It is similar to bytes, but it can be modified after creation.
# Using bytearray() function to create bytearray
value = bytearray([72, 101, 108, 108, 111])  
print(value)  
ba1 = bytearray([65, 66, 67, 68, 69]) 
print(ba1) # Output: bytearray(b'ABCDE')

#By encoding a string using "utf-8" encoding
ba2 = "Hello, World!".encode("utf-8")
print(ba2) # Output: b'Hello, World!'

#Memoryview: A memoryview is a view object that allows you to access the memory of another binary data type (like bytes or bytearray) without copying it. It provides a way to manipulate the data directly in memory, which can be more efficient for large data sets.
# Using memoryview() function to create memoryview
mv = memoryview(ba2)
print(mv) # Output: <memory at 0x...>

data = bytearray(b'Hello, world!')
view = memoryview(data)
print(view) # Output: <memory at 0x...>

# Creating memoryview using buffer interface if you have an array
import array
arr = array.array('i', [1, 2, 3, 4, 5])
mv_arr = memoryview(arr)
print(mv_arr) # Output: <memory at 0x...>

# Creating memoryview by slicing bytes or bytearray
b = b'Hello, world!'
mv_slice = memoryview(b)[0:5]
print(mv_slice) # Output: <memory at 0x...>

# Dictionaries (key-value pairs) kind of hash table types. dictionary key can be of any immutable data type (like strings, numbers, or tuples), and the values can be of any data type.
person = {"name": "Bob", "age": 30}
print("Dictionary:", person)
print("Type:", type(person))

#Sets (unordered collections of unique elements) A set is an unordered collection of unique elements. Sets are defined using curly braces {} or the set() function. They are commonly used for membership testing and eliminating duplicate entries.
fruits = {"apple", "banana", "cherry"}
print("Set:", fruits)
print("Type:", type(fruits)) #NB they may not be in the same order as they were defined because sets are unordered collections
#Only immutable data types can be added to a set, so you cannot add lists or dictionaries to a set, but you can add tuples.

#Python none type
#The None type is a special data type in Python that represents the absence of a value or a null value. It is often used to indicate that a variable has no value or that a function does not return anything.
result = None
print("None value:", result)
print("Type:", type(result))


#Setting data types
#In Python, you can set the data type of a variable using type hints. Type hints are optional and do not affect the actual behavior of the code, but they can help with code readability and provide hints to developers and tools about the expected data types.
#You can use type hints to specify the expected data type of a variable when you declare it
name: str = "Alice"
age: int = 30
height: float = 5.8
print("Name:", name)
print("Age:", age)  
print("Height:", height)
print("Type of name:", type(name))
print("Type of age:", type(age))
print("Type of height:", type(height))



# Primitive data types in Python include:
# - int: Represents integer numbers (e.g., 1, 42, -5)
# - float: Represents floating-point numbers (e.g., 3.14, -0.001)
# - bool: Represents boolean values (True or False)     
# - str: Represents strings (e.g., "Hello, World!") 

# Non-primitive data types in Python include:
# - list: Represents an ordered collection of items (e.g., [1, 2, 3], ["apple", "banana", "cherry"])
# - tuple: Represents an ordered, immutable collection of items (e.g., (1, 2, 3), ("apple", "banana", "cherry"))
# - dict: Represents a collection of key-value pairs (e.g., {"name": "Alice", "age": 30})
# - set: Represents an unordered collection of unique items (e.g., {"apple", "banana", "cherry"})   

# Python Data Type Conversion
# You can convert between different data types using built-in functions like int(), float(), str(), list(), tuple(), dict(), and set(). For example:
# Converting string to integer
num_str = "42"
num_int = int(num_str)
print("String:", num_str)
print("Integer:", num_int)
# Converting integer to float
num_float = float(num_int)
print("Integer:", num_int)
print("Float:", num_float)
# Converting float to string
num_str_from_float = str(num_float)
print("Float:", num_float)
print("String:", num_str_from_float)

#Data Type Conversion Functions
# int(): Converts a value to an integer
# float(): Converts a value to a floating-point number
# str(): Converts a value to a string
# list(): Converts a value to a list
# tuple(): Converts a value to a tuple
# dict(): Converts a value to a dictionary
# set(): Converts a value to a set
# frozenset(): Converts a value to a frozenset (an immutable set) 
# bool(): Converts a value to a boolean
# complex(): Converts a value to a complex number
# bytes(): Converts a value to a bytes object
# bytearray(): Converts a value to a bytearray object
# memoryview(): Converts a value to a memoryview object
# ord(): Converts a character to its Unicode code point (integer)
# chr(): Converts an integer to its corresponding Unicode character (string)    
# unichr(): Converts an integer to its corresponding Unicode character (string) (Python 2.x only)
# ord(): Converts a character to its Unicode code point (integer) (Python 2.x only)
# hex(): Converts an integer to a hexadecimal string
# oct(): Converts an integer to an octal string