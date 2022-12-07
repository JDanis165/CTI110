   # CTI-110
   # P3HW2 - Salary
   # Joshua Danis
   # 10/31/2022

# input ask Enter employee's name
# input ask Enter worked hours
# payrate = input pay rate
# if hours greater than 40
# do the evalution of the overtime pay and regular pay
# else the evalution of the regular pay
# reg_pay = hours_worked * pay_rate
# gross pay = regular pay + overtime pay

employname = input("Enter employee's name: ")
hours_worked= float(input("Enter number of hours worked: "))
pay_rate= float(input("Enter employee's pay rate: "))

overTime_pay = 0.0
over_time = 0.0
if hours_worked > 40:
	over_time = hours_worked - 40
	ot_payRate = pay_rate + (pay_rate * 0.5)
	overTime_pay = over_time * ot_payRate
	reg_pay = 40 * pay_rate
else:
	reg_pay = hours_worked * pay_rate

gross_pay = reg_pay + overTime_pay


print("--------------------------------------------")
print("Employee name: ", employname)
print()
print("{:<16}{:<16}{:<16}{:<16}{:<16}{:<16}".format("Hours Worked", "Pay Rate", "OverTime", "OverTime Pay", "RegHour Pay", "Gross Pay"))
print("------------------------------------------------------------------------------------------")
print("{:<16.1f}{:<16.1f}{:<16.1f}{:<16.2f}${:<16.2f}${:<16.2f}".format(hours_worked, pay_rate, over_time, overTime_pay, reg_pay, gross_pay))
