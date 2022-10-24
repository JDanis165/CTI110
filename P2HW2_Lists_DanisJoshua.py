# CTI-110
# P2HW2 - List
# Joshua Danis
# 10/17/22

# Input Module 1-6
# Grade = Module
# Sum of Grades = Module 1 + Module 2 + Module 3 + Module 4 + Module 5 + Module 6 
# Show avg of Grade
# Display min grade
# Display max Grade
# Display Sum of Grades

m1=float(input("Enter grade for Module 1:  "))
m2=float(input("Enter grade for Module 2:  "))
m3=float(input("Enter grade for Module 3:  "))
m4=float(input("Enter grade for Module 4:  "))
m5=float(input("Enter grade for Module 5:  "))
m6=float(input("Enter grade for Module 6:  "))

grades=[ ]

grades.append(m1)
grades.append(m2)
grades.append(m3)
grades.append(m4)
grades.append(m5)
grades.append(m6)

lg=min(grades)
hg=max(grades)
sg=sum(grades)
avg=sg/6

print("------------Results------------")
print("Lowest Grade:   ",lg)
print("Highest Grade:  ",hg)
print("Sum of Grades:  ",sg)
print("Average:         %.2f"%avg)

print("----------------------------------------")

