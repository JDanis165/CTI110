# CTI-110
# P3HW1 - Debugging
# Joshua Danis
# 10/26/22
# This program takes a number grade , determines average and displays letter grade for average.

# Enter grades for six modules

mod_1=float(input("Enter grade for Module 1:  "))
mod_2=float(input("Enter grade for Module 2:  "))
mod_3=float(input("Enter grade for Module 3:  "))
mod_4=float(input("Enter grade for Module 4:  "))
mod_5=float(input("Enter grade for Module 5:  "))
mod_6=float(input("Enter grade for Module 6:  "))

# add grades entered to a list

grades = [mod_1, mod_2, mod_3, mod_4, mod_5, mod_6]
# TO DO: determine lowest, highest , sum and average for grades

low = min(grades)
high = max(grades)
sum = sum(grades)
avg = sum/6

# determine letter grade for average


if avg > 90:
    grades = 'A'
elif avg > 80:
    grades = 'B'
elif avg > 70:
    grades = 'C'
elif avg > 60:
    grades = 'D'
else:
    grades = 'F' # TO DO: finish this

print("------------Results------------")
print("Lowest Grade:   ",low)
print("Highest Grade:  ",high)
print("Sum of Grades:  ",sum)
print("Average:         %.2f"%avg)

print("----------------------------------------")
print(f'Your grade is: {grades}')


