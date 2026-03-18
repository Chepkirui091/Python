#Private variables are a special type of variable that is only accessible within the class they are defined in
#Only direct access is restricted. We can define a public method to access the private variable from outside the class, it is called a getter method. Similarly, we can use a setter method to modify the value of a private variable from outside the class.
'''
Public Variables: Public variables are accessible from anywhere, both inside and outside the class. In the image, a public place is considered as an analogy for public variables as they can be accessed by anyone.
Protected Variables: Protected variable can be accessed within the class and its subclasses. In the image, a private domicile is considered as an analogy for protected variables as they can be accessed by family members (subclasses) but not by outsiders.
Private Variables: Private variables are only accessible within the class they are defined in. In the image, a vault is considered as an analogy for private variables as they can only be accessed by the owner (the class itself) and not by anyone else.
Public Variables: Public variables are accessible from anywhere, both inside and outside the class. In the image, a public place is considered as an analogy for public variables as they can be accessed by anyone.
Protected Variables: Protected variable can be accessed within the class and its subclasses. In the image, a private domicile is considered as an analogy for protected variables as they can be accessed by family members (subclasses) but not by outsiders.
Private Variables: Private variables are only accessible within the class they are defined in. In the image, a vault is considered as an analogy for private variables as they can only be accessed by the owner (the class itself) and not by anyone else.
 Similarly, a single underscore (_) is used to indicate that a variable is protected.
'''

class MyClass:
    def __init__(self):
        self.__private_variable = "This is the getter method for the private variable"
        
    def show_private(self):
        return self.__private_variable

obj = MyClass()
# print(obj.__private_var)   # ✗ AttributeError because we're trying to access directly the private variable from outside the class
print(obj.show_private())  # This will print the value of the private variable using the getter method

#Name mangling is a mechanism in Python that allows you to create private variables by prefixing the variable name with double underscores (__). This makes the variable name unique and prevents it from being accessed directly from outside the class. The variable can still be accessed using a special syntax, but it is not recommended to do so as it goes against the principle of encapsulation.
class MyClass:
    def __init__(self):
        self.__private_variable = "Testing name mangling"
        
        def show_private(self):
            return self.__private_variable
        
obj = MyClass()
# Accessing the private variable using name mangling (not recommended)
print(obj._MyClass__private_variable)  # This will print the value of the private

#PRIVATE METHODS
#Private methods are similar to private variables in that they are only accessible within the class they are defined in. They are defined using the same double underscore prefix (__) as private variables. Private methods are typically used for internal functionality that should not be exposed to users of the class.

class MyClass:
    def __init__(self):
        self.__private_variable = "This is a private variable"
        
    def __private_method(self):
        return "This is a private method"
    
    def show_private(self):
        return self.__private_variable + " and " + self.__private_method()
    
obj = MyClass()
print(obj.show_private())    # ✓ Access through method
# print(obj.__private_method())  # ✗ AttributeError
print(obj._MyClass__private_method())  # ✓ Access using name mangling

#REAL WORLLD EXAMPLE
'''
Consider a banking application where we have a class called BankAccount. This class has private variables for the account number and balance. We will define public methods to deposit, withdraw, and check the balance. We need to ensure that balance cannot be directly modified outside the class, but can only be changed through deposit and withdraw methods.
'''
class BankAccount:
    def __init__(self, account_number, balance):
        self.__account_number = account_number   # Private
        self.__balance = balance                 # Private

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
        return self.__balance

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
        return self.__balance

    def get_balance(self):
        return self.__balance

account = BankAccount("12345", 1000)

# Direct access will fail
try:
    account.__balance += 500  # ✗ AttributeError
except AttributeError:
    print("Direct access to private variable failed!!!")

# Access using methods
print("Your account balance is: ", account.get_balance())   # ✓ 1000

account.deposit(500)
print("Your account balance after deposit is: ", account.get_balance())  # ✓ 1500