# Author: Amit Singh Mehmi
# Date: October 29th, 2021
#
# This code will be an interface for runners to calculate their splits for specific events that they
# would like to run

from time import sleep

# Input stage of interface and calculation

def main():

    print("\nWelcome To The Runner's Interface")
    sleep(1)
    userName = input("\nWhat is your name?: ")
    sleep(1)
    print("Okay," + userName + "...")
    sleep(1)
    userEvent = (int(input("\nWhat is your running event in meters?: ")))
    sleep(0.8)
    userSplits = (int(input("At what splits wold you like to know? (meters): ")))
    sleep(1)
    print("\nSounds good,", userName, "!", "At what time would you like to accomplish", userEvent, "meters in?")
    sleep(1)
    userSeconds = (int(input("Please enter desired seconds: ")))
    userMinutes = (int(input("Please enter desired minutes: ")))
    userHour = (int(input("Please enter desired hours: ")))
    sleep(1)
    print("\nAlrighty,", userName, "calculation in progress...")

    # Calculation process

    timeCalculation = userMinutes * 60 + userSeconds + userHour * 3600
    distanceCalculation = timeCalculation / userEvent
    splitsCalculation = distanceCalculation * userSplits
    if splitsCalculation >= 60 and splitsCalculation < 3600:
        splitsCalculationMinutes = int(splitsCalculation // 60)
        splitsCalculationSeconds = (splitsCalculation - 60 * splitsCalculationMinutes)
        splitsoverall = splitsCalculationMinutes, str("minutes"), (format(splitsCalculationSeconds, ".2f")) +str(" seconds")
    elif splitsCalculation == 3600:
        splitsCalculationHours = int(splitsCalculation // 3600)
        splitsCalculationMinutes = int(splitsCalculation // 60 - 60)
        splitsCalculationSeconds = (splitsCalculation - 3600)
        splitsoverall = splitsCalculationHours, str("hours"), splitsCalculationMinutes, str("minutes"), (format(splitsCalculationSeconds, ".2f")) + str(" seconds")
    elif splitsCalculation >= 3600:
        splitsCalculationHours = int(splitsCalculation // 3600)
        splitsCalculationMinutes = int(splitsCalculation // 60 - 60)
        splitsCalculationSeconds = ((splitsCalculation - 3600) - 60)
        splitsoverall = splitsCalculationHours, str("hours"), splitsCalculationMinutes, str("minutes"), (format(splitsCalculationSeconds, ".2f")) + str(" seconds")
    else:
        splitsoverall = (format(splitsCalculation, ".2f")) + str(" seconds")

    # Output stage

    sleep(3)
    print("To run", userEvent, "meters in: ")
    sleep(1)
    print(userHour, "hours", userMinutes, "minutes", userSeconds, "seconds")
    sleep(1)
    print("Your split every", userSplits, "meters should be in:")
    sleep(1)
    print(splitsoverall)
    sleep(2)

    restartInterface = input("\nThank you for using the Runner's Interface! Would you like to restart?(type yes or no): ")
    if restartInterface == "yes":
        main()
    else:
        print("Thank you! Come again!")

main()
