# Control Flow is controlled by various conditional statements and loops and function calls.
# By default, instructions are executed sequentially: the first instruction in a function is executed first, followed by the second, and so on.
# We can use control flow statements to change the order of execution of instructions or to execute certain instructions only under certain conditions.

# DECISION MAKING STATEMENTS
# Decision making statements are used to make decisions based on certain conditions. They include if statements, if-else statements, and if-elif-else statements.

# The if statement is used to execute a block of code only if a certain condition is true. For example:
x = 10
if x > 5:
    print("x is greater than 5.")
    

# The if-else statement is used to execute one block of code if a certain condition is true and another block of code if the condition is false. For example:
age = 18
if age >= 18:
    print("You are an adult.")
else:
    print("You are a minor.")
    
# The if-elif-else statement is used to execute one block of code among multiple blocks of code based on different conditions. For example:
marks = 85
result = ""
if marks >= 90:
    result = "Grade: A"
elif marks >= 80:
    result = "Grade: B"
elif marks >= 70:
    result = "Grade: C"
else:
    result = "Grade: F"
    
print(result)  

# The match statement is a new control flow statement introduced in Python 3.10. It allows you to match a value against a series of patterns and execute code based on the first pattern that matches. This can be useful for simplifying complex conditional logic and improving readability in certain situations.
# For example, you can use the match statement to handle different cases based on the value of a variable:

command = "start"
match command:
    case "start":
        print("Starting the process...")
    case "stop":
        print("Stopping the process...")
    case "pause":
        print("Pausing the process...")
    case _:
        print("Unknown command.")
        
def checkVowel(n):
    match n:
        case 'a': return "Vowel"
        case 'e': return "Vowel"
        case 'i': return "Vowel"
        case 'o': return "Vowel"
        case 'u': return "Vowel"
        case _: return "Consonant"
print(checkVowel('a'))  # Output: Vowel
print(checkVowel('b'))  # Output: Consonant


# LOOPS OR ITERATION STATEMENTS
# Loops are used to execute a block of code repeatedly until a certain condition is met. They include for loops and while loops.

# For loops are used to iterate over a sequence (such as a list, tuple, or string) or other iterable objects. For example:
words = ["one", "two", "three"]
for x in words:
    print(x)
    
# While loops are used to execute a block of code as long as a certain condition is true. For example:
i = 1
while i <= 5:
    print(i)
    i += 1
    
# Jump statements are used to control the flow of loops. They include break, continue, and pass statements.

# The break statement is used to exit a loop prematurely when a certain condition is met. For example:
x = 0
while x < 10:
    print("x:" , x)
    if x == 5:
        print("Breaking...")
        break
    x += 1
    
print("End")

# The continue statement is used to skip the current iteration of a loop and move on to the next iteration. For example:
for letter in "Python":
    if letter == "h":
        continue
    print(("Current Letter: "), letter)
    
