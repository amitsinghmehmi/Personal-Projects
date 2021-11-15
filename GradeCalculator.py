# Author: Amit Singh Mehmi
# Date: November 14th, 2021
#
# This program will take the user's grades and provide an average and letter as the output
#

def grade_calculator():

    import time

# List of all user's grades
    user_grades = []

    print("\nWelcome to the grades calculator!")
    time.sleep(2)

# Input Stage
    user_number_of_grades = (int(input("\nHow many grades do you have?: ")))

    for grades in range(user_number_of_grades):
        user_grades.append(int(input("Enter Grade: ")))

# Calculation Stage
    print("Calculating your grade...")
    user_final = sum(user_grades)
    user_final = int(user_final / user_number_of_grades)

# Output Stage
    time.sleep(3)
    print(f"Your final grade is: {user_final}%")

    if user_final >= 95:
        print("\nYou passed with an A+! Congrats!")

    if 85 <= user_final <= 94:
        print("\nYou passed with an A! Congrats!")

    if 80 <= user_final <= 84:
        print("\nYou passed with an A-! Congrats!")

    if 78 <= user_final <= 79:
        print("\nYou passed with an B+! Congrats!")

    if 75 <= user_final <= 77:
        print("\nYou passed with an B! Congrats!")

    if 70 <= user_final <= 74:
        print("\nYou passed with an B-! Congrats!")

    if 68 <= user_final <= 69:
        print("\nYou passed with an C+! Congrats!")

    if 65 <= user_final <= 67:
        print("\nYou passed with an C! Congrats!")

    if 60 <= user_final <= 64:
        print("\nYou passed with an C-! Congrats!")

    if 58 <= user_final <= 59:
        print("\nYou passed with an D+! Congrats!")

    if 55 <= user_final <= 57:
        print("\nYou passed with an D! Congrats!")

    if 50 <= user_final <= 54:
        print("\nYou passed with an D-! Congrats!")

    if user_final <= 50:
        print("Sorry you have failed! Better luck next time")

grade_calculator()

# Restarting/Ending Stage
restart = (input("\nWould you like to calculate your grades again?(type yes): "))

if restart == "yes":
    grade_calculator()
else:
    print("Thank you for using the calculator, come again next time! ")
