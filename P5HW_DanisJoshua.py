# Generates Math quizzes for user ranging between 1-100, using various forms of maths such as subtraction and addition
# 11/22/2022
# CTI-110 P5HW2 - Math Quiz
# Joshua Danis



import random
def Addition():
    # Gathering random integers in range 1 to 100
    a = random.randint(1,100)
    b = random.randint(1,100)
    print("   ",a)
    print(" + ",b)
    # Calculating our sum
    sum = a+b
    # Asking for user answer
    answer = int(input("\nEnter answer: "))
    guess = 1
    # loop for getting answer while answer is not correct
    while sum!=answer:
        # if answer less than sum print it is too low
        if answer<sum:
            print("Sorry, guess is too low.")
        # if answer more than sum print it is too high
        else:
            print("Sorry, guess is too high.")
        # again getting user input
        answer = int(input("\ntry again: "))
        guess+=1
    # printing congratulation if answer is correct
    print("Congratulations!!!! your answer is correct..")
    # printing number of gueses
    print("Number of guesses: ",guess)

def Subtraction():
    # Gathering random integers in range 1 to 100
    a = random.randint(1, 100)
    b = random.randint(1, 100)
    print("   ", a)
    print(" - ", b)
    # calculating difference
    diff = a - b
    # asking for user answer
    answer = int(input("\nEnter answer: "))
    guess = 1
    # loop for getting answer while answer is not correct
    while diff != answer:
        # if answer less than diff print it is too low
        if answer < diff:
            print("Sorry, guess is too low.")
        # if answer more than diff print it is too high
        else:
            print("Sorry, guess is too high.")
        # again getting user input
        answer = int(input("\ntry again: "))
        # incrementing the count of gueses
        guess += 1
    # printing congratulation if answer is correct
    print("Congratulations!!!! your answer is correct..")
    # printing number of gueses
    print("Number of guesses: ",guess)

# function to display menu and get user choice
def main():
    # displaying menu
    print("\nMAIN MENU")
    print("-"*20)
    print("1. Adding Random Numbers")
    print("2. Subtracting Random Numbers")
    print("3. Exit\n")
    # getting user input
    option = int(input("Please choose one of the menu options: "))
    # if option equals to 1 call Addition() function
    if option==1:
        Addition()    
    elif option==2:
        Subtraction()
    elif option == 3:
        print("Thank you for playing...")
        print("Bye!!")
        exit()
    else:
        print("Invalid option. Please choose again")
    main()


print("Welcome to the Math Quiz\n")
main()