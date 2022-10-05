# Asking for the input of 4 float values from the user
num1 = float(input())
num2 = float(input())
num3 = float(input())
num4 = float(input())


# using the f-strings we can print the product of the numbers and average of numbers with 0 digits precision
print(f'{num1 * num2 * num3 * num4:.0f} {((num1 + num2 + num3 + num4) / 4):.0f}')
# Once again using f-strings we can printing product of the numbers and average of numbers with 3 digits precision
print(f'{num1 * num2 * num3 * num4:.3f} {((num1 + num2 + num3 + num4) / 4):.3f}')
