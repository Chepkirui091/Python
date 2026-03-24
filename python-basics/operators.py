# Python operators are special symbols that perform specific operations on one or more operands. They are used to manipulate data and variables in Python. Here are some common types of operators in Python:
# Terms used in operators:
# Operand: Variables, values, or expressions that are used with the operator to perform a specific operation.
# Unary Operator: Python operators that require one operand to perform a specific operation are known as unary operators. For example, the negation operator (-) is a unary operator that negates the value of its operand.
# Binary Operator:  Python operators that require two operands to perform a specific operation are known as binary operators. For example, the addition operator (+ is a binary operator that adds two operands together.

# Types of operators in Python:
# Arithmetic Operators: These operators are used to perform mathematical operations such as addition, subtraction, multiplication, division, modulus, exponentiation, and floor division.
a = 10
b = 5
c = a + b  # Addition
d = a - b  # Subtraction
e = a * b  # Multiplication
f = a / b  # Division
g = a % b  # Modulus
h = a ** b # Exponentiation
i = a // b # Floor division

# Comparison Operators: These operators are used to compare two values and return a boolean result (True or False). They include equality (==), inequality (!=), greater than (>), less than (<), greater than or equal to (>=), and less than or equal to (<=).
x = 10
y = 5
z = x == y  # Equality
w = x != y  # Inequality
v = x > y   # Greater than
u = x < y   # Less than
t = x >= y  # Greater than or equal to
s = x <= y  # Less than or equal to

# Logical Operators: These operators are used to combine multiple boolean expressions and return a boolean result. They include logical AND (and), logical OR (or), and logical NOT (not).
p = True
q = False
r = p and q  # Logical AND
s = p or q   # Logical OR
t = not p    # Logical NOT

# Assignment Operators: These operators are used to assign values to variables. They include the basic assignment operator (=) and compound assignment operators such as +=, -=, *=, /=, %=, **=, and //=.
m = 10
n = 5
m += n  # Equivalent to m = m + n
m -= n  # Equivalent to m = m - n
m *= n  # Equivalent to m = m * n
m /= n  # Equivalent to m = m / n
m %= n  # Equivalent to m = m % n
m **= n # Equivalent to m = m ** n # raised to the power of n
m //= n # Equivalent to m = m // n # Equivalent to m = m // n # floor division and assignment. if both are positive, it behaves like regular floor division. However, if either operand is negative, the result is rounded down to the nearest integer that is less than or equal to the result of the division.

# Bitwise Operators: These operators are used to perform bitwise operations on integers. They include bitwise AND (&), bitwise OR (|), bitwise XOR (^), bitwise NOT (~), left shift (<<), and right shift (>>).
a = 5  # In binary: 0101    
b = 3  # In binary: 0011
c = a & b  # Bitwise AND
d = a | b  # Bitwise OR
e = a ^ b  # Bitwise XOR
f = ~a     # Bitwise NOT
g = a << 1 # Left shift
h = a >> 1 # Right shift

# Identity Operators: These operators are used to compare the memory locations of two objects. They include the identity operator (is) and the negation of the identity operator (is not).
x = [1, 2, 3]
y = [1, 2, 3]
z = x is y  # Identity operator
w = x is not y  # Negation of identity operator

# Membership Operators: These operators are used to test whether a value is present in a sequence (such as a list, tuple, or string). They include the membership operator (in) and the negation of the membership operator (not in).
my_list = [1, 2, 3, 4, 5]
z = 3 in my_list  # Membership operator
w = 6 not in my_list  # Negation of membership operator 

# Walrus Operator: The walrus operator (:=) is a new assignment expression operator introduced in Python 3.8. It allows you to assign a value to a variable as part of an expression. This can be useful for reducing the number of lines of code and improving readability in certain situations.
# For example, you can use the walrus operator to assign a value to a variable while checking a condition in an if statement:
if (n := len(my_list)) > 3:
    print(f"The list has {n} elements, which is greater than 3.")
    
    
# Traditional way
print("Using traditional way:")
stack = [1, 2, 3, 4, 5]
n = len(stack)
while len(stack) > 0:
    print(stack.pop(), end=" ")
print("\n\n")

# Simplify using walrus operator
print("Using walrus operator:")
stack = [1, 2, 3, 4, 5]
while (n := len(stack)) > 0:
    print(stack.pop(), end=" ")
    print(f"Remaining elements: {n}")