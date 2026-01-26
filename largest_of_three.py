# largest_of_three.py
# Inputs three integers, uses nested ifs to find largest

# Input: Get three integers from user
num1 = int(input("Enter first integer: "))
num2 = int(input("Enter second integer: "))
num3 = int(input("Enter third integer: "))

# Process: Nested if statements to find largest
largest = num1
if num2 > largest:
    largest = num2
if num3 > largest:
    largest = num3

# Output: Display the largest number
print("Largest:", largest)


# # largest_of_three.py - Chapter 3 chained/nested conditionals
# num1 = int(input("Enter first integer: "))
# num2 = int(input("Enter second integer: "))
# num3 = int(input("Enter third integer: "))
#
# # Method 1: Nested ifs
# # what is the largest input
# largest = num1
# if num2 > largest:
#     largest = num2
# if num3 > largest:
#     largest = num3
#
# # Method 2: Chained conditionals
# # This is written to tell which ordered input is largest
# print("Largest (nested):", largest)
#
# if num1 >= num2 and num1 >= num3:
#     print("Largest (chained 1):", num1)
# elif num2 >= num1 and num2 >= num3:
#     print("Largest (chained 2):", num2)
# else:
#     print("Largest (chained 3):", num3)  # else 【
