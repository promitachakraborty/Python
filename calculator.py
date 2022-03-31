import math


def add(num1, num2):
    # This function is used for adding two numbers
            return num1 + num2


def subtract(num1, num2):
    # This function is used for subtracting two numbers
            return num1 - num2


def multiply(num1, num2):
    # This function is used for multiplying two numbers
           return num1 * num2


def divide(num1, num2):
    # This function is used for dividing two numbers
           return num1 / num2

def mod(num1, num2):
           return num1 % num2

def square_root(num1):
    # This function is used for dividing two numbers
           return num1 ** 0.5

def cube_root(num1):

           return num1 ** (1 / 3)

def exponent(num1 , num2):
          return num1 ** num2

def tan(num1):
          return(tan(num1))

def sin(num1):
         return(sin(num1))

def cos(num1):
        return(cos(num1))

def log(num1):
         return(log(num1))

# Now we will take inputs from the user
print("Please select the operation.")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
print("5. Modules")
print("6. Square_Root")
print("7. Cube_Root")
print("8. exponent")
print("9. Tan")
print("10. Sin")
print("11. Cos")
print("12. Log")

choice = input("Please enter choice (1/2/3/4/5/6/7/8/9/10/11/12): ")



if choice == '1':
    num_1 = int(input("Please enter the first number: "))
    num_2 = int(input("Please enter the second number: "))
    print(num_1, " + ", num_2, " = ", add(num_1, num_2))

elif choice == '2':
    num_1 = int(input("Please enter the first number: "))
    num_2 = int(input("Please enter the second number: "))
    print(num_1, " - ", num_2, " = ", subtract(num_1, num_2))

elif choice == '3':
    num_1 = int(input("Please enter the first number: "))
    num_2 = int(input("Please enter the second number: "))
    print(num1, " * ", num2, " = ", multiply(num1, num2))
elif choice == '4':
    num_1 = int(input("Please enter the first number: "))
    num_2 = int(input("Please enter the second number: "))
    print(num_1, " / ", num_2, " = ", divide(num_1, num_2))
elif choice == '5':
    num_1 = int(input("Please enter the first number: "))
    num_2 = int(input("Please enter the second number: "))
    print(num_1, " % ", num_2, " = ", mod(num_1, num_2))
elif choice == '6':
    num_1 = int(input("Please enter the a number: "))

    print(num_1, " ** ",  " = ", square_root(num_1))

elif choice == '7':
    num_1 = int(input("Please enter the a number: "))

    print(num_1,"**(1/3)","=", cube_root(num_1))

elif choice == '8':
    num_1 = int(input("Please enter the first number: "))
    num_2 = int(input("Please enter the second number: "))
    print(num_1,"**", num_2,"=", exponent(num_1,num_2))
elif choice == '9':
    num_1 = int(input("Please enter a number:"))
    print(math.tan(num_1))
elif choice == '10':
    num_1 = int(input("Please enter a number:"))
    print(math.sin(num_1))
elif choice == '11':
    num_1 = int(input("Please enter a number:"))
    print(math.cos(num_1))
elif choice == '12':
    num_1 = int(input("Please enter a number:"))
    print(math.log(num_1))

else:
    print("This is an invalid input")
