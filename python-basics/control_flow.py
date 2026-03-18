# Control Flow in Python
# Using if statements and loops

# If statements
age = 18

if age >= 18:
    print("You are an adult")
else:
    print("You are a minor")

# If-elif-else
score = 85

if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
else:
    print("Grade: F")

# For loop
print("\nCounting with for loop:")
for i in range(1, 6):
    print(i)

# While loop
print("\nCounting with while loop:")
count = 1
while count <= 5:
    print(count)
    count += 1

# Loop through a list
fruits = ["apple", "banana", "orange"]
print("\nFruits:")
for fruit in fruits:
    print(fruit)