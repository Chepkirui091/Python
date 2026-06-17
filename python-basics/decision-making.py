# Let us consider an example of a customer entitled to 10% discount if his purchase amount is > 1000; if not, then no discount is applicable. The following flowchart shows the whole decision making process −
amount = int(input("Enter the purchase amount: "))
if amount > 1000:
    discount = amount * 0.1
    final_amount = amount - discount
    print("You are eligible for a 10% discount.")
    print("Final amount to be paid: ", final_amount)
else:
    print("You are not eligible for a discount.")
    print("Final amount to be paid: ", amount)
    
# If the expression age > 18 is true, then eligible to vote message will be displayed otherwise not eligible to vote message will be displayed. Following flowchart illustrates this logic −
age = int(input("Enter your age: "))
if age > 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")
    
'''
Suppose there are different slabs of discount on a purchase −

20% on amount exceeding 10000,

10% for amount between 5-10000,

5% if it is between 1 to 5000.

no discount if amount<1000
'''

amount = int(input("Enter the purchase amount: "))
if amount > 10000:
    discount = amount * 0.2
elif amount > 5000:
    discount = amount * 0.1
elif amount > 1000:
    discount = amount * 0.05
else:
    discount = 0
    
final_amount = amount - discount
print("Final amount to be paid: ", final_amount)


# Nested if statements are if statements inside another if statement. They are used to check multiple conditions in a hierarchical manner. For example:
# Suppose we want to check if a number is divisible by both 2 and 3. We can use nested if statements to check this condition:
number = int(input("Enter a number: "))
if number % 2 == 0:
    if number % 3 == 0:
        print("The number is divisible by both 2 and 3.")
    else:
        print("The number is divisible by 2 but not by 3.")
else:
    if number % 3 == 0:
        print("The number is divisible by 3 but not by 2.")
    else:
        print("The number is not divisible by either 2 or 3.")  