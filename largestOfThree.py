# largestOfThree.py
# Program to find the largest of three integers using nested if statements

# Get three integers from the user
num1 = int(input("Enter the first integer: "))
num2 = int(input("Enter the second integer: "))
num3 = int(input("Enter the third integer: "))

# Use nested if statements to find the largest
if num1 >= num2:
    if num1 >= num3:
        print(f"The largest number is {num1}")
    else:
        print(f"The largest number is {num3}")
else:
    if num2 >= num3:
        print(f"The largest number is {num2}")
    else:
        print(f"The largest number is {num3}")