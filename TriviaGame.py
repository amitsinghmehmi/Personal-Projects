# Author: Amit Singh Mehmi
# Date: February 3rd, 2021
#
# Description: This program is simillar to a Who Wants to Be a Millionare game. However, in this program/game, you are given two lives and two lifelines.
# Answering questions right will win you money depending on how far you advance in the levels. Typing in lifeline as the answer will give you a hint if
# you are stuck, this can be used twice in a question if you are really stuck. If you run out of lives, you lose all the money you gained and are prompted
# to enter if you want to play again, as well as showing how many question you got right


def main():  # (Defining a Function learnt from: https://cscircles.cemc.uwaterloo.ca/10-def/)
    # This is a function definition that defines the starting point for the program

    from time import sleep  # (Sleep from Time module learnt from: https://docs.python.org/3/library/time.html)
    # This essientially suspends the execution of the next thread depending on the given seconds

    # Known Variables (All the things we already know before starting the game)

    answer = "yes"
    moneyMade = 0
    outputMessageGain = "\nCorrect! You gained: ${:.2f} \nYour total grand prize is now: ${:.2f}"
    outputMessageLoss = "\nThank you for playing, Who Wants to be a Millionare!"
    outputMessageLifeline = "\nYou have used a lifeline, You now have: "
    levelOne = 1000
    levelTwo = 3000
    levelThree = 5000
    levelFour = 10000
    levelFive = 15000
    levelSix = 30000
    levelSeven = 60000
    levelEight = 100000
    levelNine = 500000
    levelTen = 1000000
    LifeLine = 2
    lives = 2
    score = 0

    # While loop (Essientially the starting of the game that continues as long as conditions hold true)

    while answer == "yes" and lives > 0:

        # Host's introduction (The sleep function between each string allows for a more realistic and user-friendly experience)
        # Host inspiration from: https://repl.it/talk/share/Game-Who-Wants-To-Be-A-Millionaire/6162

        print("\nThis is a new round of...")
        sleep(0.6)
        print("\nWho")
        sleep(0.6)
        print("Wants")
        sleep(0.6)
        print("To")
        sleep(0.6)
        print("Be")
        sleep(0.6)
        print("A")
        sleep(0.6)
        print("MILLIONAIRE?!")
        sleep(1.2)
        print("\n*audience roaring*")
        sleep(3)

        print("\nOur first contestant is ....")
        sleep(1.5)
        print("......")
        sleep(1.5)
        name = input("\nApologies. What is your name? (enter your name): ")  # User enters their name
        print("Lovely to meet you!")
        sleep(2)

        # Host introduces game rules to user (lifelines, lives, how to answer and the moneyboard)

        print("\nAlrighty,", name, "!", " Let's get started. A reminder: You have two lifelines and two lives!")
        sleep(4)
        print("\nIf you ever need a lifeline/hint type in lifeline (*lowercase) as the answer.")
        sleep(5)
        print("If you know the answer type in the letter option (*lowercase) as the answer.")
        sleep(5)
        print("\nBelow is the Money Board! It shows how much each level can give you!")
        sleep(3)
        print("\n                   MONEY BOARD")
        sleep(0.7)
        print("                  -------------")
        sleep(1)
        print("               Level 1  |  $1,000")
        sleep(1)
        print("               Level 2  |  $3,000")
        sleep(1)
        print("               Level 3  |  $5,000")
        sleep(0.7)
        print("               Level 4  |  $10,000")
        sleep(0.7)
        print("               Level 5  |  $15,000")
        sleep(0.7)
        print("               Level 6  |  $30,000")
        sleep(0.5)
        print("               Level 7  |  $60,000")
        sleep(0.5)
        print("               Level 8  |  $100,000")
        sleep(0.5)
        print("               Level 9  |  $500,000")
        sleep(0.5)
        print("             Level 10   |  $1,000,000")
        sleep(5)

        # Question 1
        # Question 1 being presented to user:

        answerOne = (str(input(
            "\nLevel One ($1000):            How Many Laps Are in a 800m Race?\n                              ---------------------------------\n                              (a) 1 lap             (b) 3 laps\n                              (c) 4 laps            (d) 2 laps\nAnswer: ")))

        # if statements of the answer they give, either lifeline, correct answer or wrong answer
        # however since we don't know how many times the user will need a lifeline, there are if statements for the different situations

        if answerOne == "d":  # Correct answer
            sleep(0.7)
            print(outputMessageGain.format(levelOne, levelOne))  # Correct answer message
            moneyMade += levelOne
            score += 1  # += refers to score = score + 1 or variable = variable + 1
        elif answerOne == "lifeline" and LifeLine > 0:  # Lifeline
            LifeLine -= 1  # -= refers to score = score - 1 or variable = variable - 1
            sleep(1)
            print("\nYou have used a lifeline, \nYou now have", LifeLine, " lifeline remaining")
            sleep(2)
            print("\nHint: 400m = 1 lap")  # Hint
            sleep(3)
            answerOne = (str(input(
                "\nLevel One ($1000):            How Many Laps Are in a 800m Race?\n                              ---------------------------------\n                              (a) 1 lap             (b) 3 laps\n                              (c) 4 laps            (d) 2 laps\nAnswer: ")))
            if answerOne == "d":  # Correct answer
                sleep(0.7)
                print(outputMessageGain.format(levelOne, levelOne))  # Correct answer message
                moneyMade += levelOne
                score += 1
            elif answerOne == "lifeline" and LifeLine > 0:  # Lifeline #2 (if they decide to)
                LifeLine -= 1
                sleep(1)
                print("\nYou have used a lifeline, \nYou now have", LifeLine, " lifeline remaining")
                sleep(2)
                print("\nHint: 800m = 400mx2")  # Hint #2
                sleep(3)
                answerOne = (str(input(
                    "\nLevel One ($1000):            How Many Laps Are in a 800m Race?\n                              ---------------------------------\n                              (a) 1 lap             (b) 3 laps\n                              (c) 4 laps            (d) 2 laps\nAnswer: ")))
                if answerOne == "d":  # Correct answer
                    sleep(0.7)
                    print(outputMessageGain.format(levelOne, levelOne))  # Correct answer message
                    moneyMade += levelOne
                    score += 1

                # If statements for when the user doesn't enter it correct

                elif answerOne != "d":
                    sleep(0.7)
                    print("\nSorry", name, "! You selected the wrong answer!")
                    lives = lives - 1
            elif answerOne != "d":
                sleep(0.7)
                print("\nSorry", name, "! You selected the wrong answer!")
                lives = lives - 1

        elif answerOne != "d":
            sleep(0.7)
            print("\nSorry", name, "! You selected the wrong answer!")
            lives = lives - 1

        # Whatever their answer, after every input, the user will get the remaining amount of lives and lifelines

        sleep(1)
        print("\nYou have", lives, "lives remaining")
        sleep(0.7)
        print("You have", LifeLine, "lifeline remaining")

        # Question 2
        # Question 2 being presented to user:

        sleep(2)
        answerTwo = (str(input(
            "\nLevel Two ($3000):            What Part of the Atom Has No Charge?\n                              ------------------------------------\n                              (a) Proton            (b) Neutron\n                              (c) Electron          (d) ion\nAnswer: ")))

        # if statements of the answer they give, either lifeline, correct answer or wrong answer
        # however since we don't know how many times the user will need a lifeline, there are if statements for the different situations

        if answerTwo == "b":
            sleep(0.7)
            print(outputMessageGain.format(levelTwo - moneyMade, levelTwo))
            moneyMade = levelTwo
            score += 1
        elif answerTwo == "lifeline" and LifeLine > 0:
            LifeLine -= 1
            sleep(1)
            print("\nYou have used a lifeline, \nYou now have", LifeLine, " lifeline remaining")
            sleep(2)
            print("\nHint: It is nuetral")
            sleep(3)
            answerTwo = (str(input(
                "\nLevel Two ($3000):            What Part of the Atom Has No Charge?\n                              ------------------------------------\n                              (a) Proton            (b) Neutron\n                              (c) Electron          (d) ion\nAnswer: ")))
            if answerTwo == "b":
                sleep(0.7)
                print(outputMessageGain.format(levelTwo - moneyMade, levelTwo))
                moneyMade = levelTwo
                score += 1
            elif answerTwo == "lifeline" and LifeLine > 0:
                LifeLine = LifeLine - 1
                sleep(1)
                print("\nYou have used a lifeline, \nYou now have", LifeLine, " lifeline remaining")
                sleep(2)
                print("\nHint: Proton(+) Neutron(-+) Electron(-)")
                sleep(3)
                answerTwo = (str(input(
                    "\nLevel Two ($3000):            What Part of the Atom Has No Charge?\n                              ------------------------------------\n                              (a) Proton            (b) Neutron\n                              (c) Electron          (d) ion\nAnswer: ")))
                if answerTwo == "b":
                    sleep(0.7)
                    print(outputMessageGain.format(levelTwo - moneyMade, levelTwo))
                    moneyMade = levelTwo
                    score += 1
                elif answerTwo != "b":
                    sleep(0.7)
                    print("\nSorry", name, "! You selected the wrong answer!")
                    lives = lives - 1
            elif answerTwo != "b":
                sleep(0.7)
                print("\nSorry", name, "! You selected the wrong answer!")
                lives = lives - 1

        elif answerTwo != "b":
            sleep(0.7)
            print("\nSorry", name, "! You selected the wrong answer!")
            lives = lives - 1

        # Again the user will be shown their lives and lifelines

        sleep(1)
        print("\nYou have", lives, "lives remaining")
        sleep(0.7)
        print("You have", LifeLine, "lifeline remaining")

        # Question 3
        # Question 3 being presented to the user:

        sleep(2)
        answerThree = (str(input(
            "\nLevel Three ($5000):             What is the Capital of Canada?\n                                ------------------------------\n                                (a) Ottawa            (b) Toronto\n                                (c) Vancouver         (d) Montreal\nAnswer: ")))

        # Simillarly the if statements

        if answerThree == "a":
            sleep(0.7)
            print(outputMessageGain.format(levelThree - moneyMade, levelThree))
            moneyMade = levelThree
            score += 1
        elif answerThree == "lifeline" and LifeLine > 0:
            LifeLine -= 1
            sleep(1)
            print("\nYou have used a lifeline, \nYou now have", LifeLine, " lifeline remaining")
            sleep(2)
            print("\nHint: It is located in Ontario")
            sleep(3)
            answerThree = (str(input(
                "\nLevel Three ($5000):             What is the Capital of Canada?\n                                ------------------------------\n                                (a) Ottawa            (b) Toronto\n                                (c) Vancouver         (d) Montreal\nAnswer: ")))
            if answerThree == "a":
                sleep(0.7)
                print(outputMessageGain.format(levelThree - moneyMade, levelThree))
                moneyMade = levelThree
                score += 1
            elif answerThree == "lifeline" and LifeLine > 0:
                LifeLine = LifeLine - 1
                sleep(1)
                print("\nYou have used a lifeline, \nYou now have", LifeLine, " lifeline remaining")
                sleep(2)
                print("\nHint: It starts with a vowel")
                sleep(3)
                answerThree = (str(input(
                    "\nLevel Three ($5000):             What is the Capital of Canada?\n                                ------------------------------\n                                (a) Ottawa            (b) Toronto\n                                (c) Vancouver         (d) Montreal\nAnswer: ")))
                if answerThree == "a":
                    sleep(0.7)
                    print(outputMessageGain.format(levelThree - moneyMade, levelThree))
                    moneyMade = levelThree
                    score += 1
                elif answerThree != "a":
                    sleep(0.7)
                    print("\nSorry", name, "! You selected the wrong answer!")
                    lives = lives - 1
            elif answerThree != "a":
                sleep(0.7)
                print("\nSorry", name, "! You selected the wrong answer!")
                lives = lives - 1

        elif answerThree != "a":
            sleep(0.7)
            print("\nSorry", name, "! You selected the wrong answer!")
            lives = lives - 1

        # Lives and lifelines remaining

        sleep(1)
        print("\nYou have", lives, "lives remaining")
        sleep(0.7)
        print("You have", LifeLine, "lifeline remaining")

        # Since its impossible to lose the game in the first two questions, the user can run out of lives after and including the third question
        # Running out of lives will show their score or how many they got right and will be asked if they want to play again

        if lives < 0:
            sleep(0.7)
            print("\nYou got", score, "out of 10 correct!")
            sleep(1)
            answer = input("\nYou ran out of lives! Play again? Enter yes/no: ")
            if answer == "no":
                break  # This break variable essientially breaks the while loop and executes whatever is remaining on the outside
            if answer == "yes":
                main()  # This is the same main function in the beginning. This replays the main function that was defined in the beginning. The defintition being this game. Meaning it will start the game over if the user enters yes

        # Question 4
        # Question 4 being presented to the user

        sleep(2)
        answerFour = (str(input(
            "\nLevel Four ($10000):          Which Planet is the Hottest?\n                              ----------------------------\n                              (a) Mercury            (b) Mars\n                              (c) Saturn             (d) Venus\nAnswer: ")))

        # If statements

        if answerFour == "d":
            sleep(0.7)
            print(outputMessageGain.format(levelFour - moneyMade, levelFour))
            moneyMade = levelFour
            score += 1
        elif answerFour == "lifeline" and LifeLine > 0:
            LifeLine -= 1
            sleep(1)
            print("\nYou have used a lifeline, \nYou now have", LifeLine, " lifeline remaining")
            sleep(2)
            print("\nHint: It is the 2nd planet to the sun")
            sleep(3)
            answerFour = (str(input(
                "\nLevel Four ($10000):          Which Planet is the Hottest?\n                              ----------------------------\n                              (a) Mercury            (b) Mars\n                              (c) Saturn             (d) Venus\nAnswer: ")))
            if answerFour == "d":
                sleep(0.7)
                print(outputMessageGain.format(levelFour - moneyMade, levelFour))
                moneyMade = levelFour
                score += 1
            elif answerFour == "lifeline" and LifeLine > 0:
                LifeLine = LifeLine - 1
                sleep(1)
                print("\nYou have used a lifeline, \nYou now have", LifeLine, " lifeline remaining")
                sleep(2)
                print("\nHint: My Very Educated Mother Just Served Us Noodles, MVEMJSUN")
                sleep(3)
                answerFour = (str(input(
                    "\nLevel Four ($10000):          Which Planet is the Hottest?\n                              ----------------------------\n                              (a) Mercury            (b) Mars\n                              (c) Saturn             (d) Venus\nAnswer: ")))
                if answerFour == "d":
                    sleep(0.7)
                    print(outputMessageGain.format(levelFour - moneyMade, levelFour))
                    moneyMade = levelFour
                    score += 1
                elif answerFour != "d":
                    sleep(0.7)
                    print("\nSorry", name, "! You selected the wrong answer!")
                    lives = lives - 1
            elif answerFour != "d":
                sleep(0.7)
                print("\nSorry", name, "! You selected the wrong answer!")
                lives = lives - 1

        elif answerFour != "d":
            sleep(0.7)
            print("\nSorry", name, "! You selected the wrong answer!")
            lives = lives - 1

        # Lives and lifelines remaining

        sleep(1)
        print("\nYou have", lives, "lives remaining")
        sleep(0.7)
        print("You have", LifeLine, "lifeline remaining")

        # If user has no lives left

        if lives < 0:
            sleep(0.7)
            print("\nYou got", score, "out of 10 correct!")
            sleep(1)
            answer = input("\nYou ran out of lives! Play again? Enter yes/no: ")
            if answer == "no":
                break
            if answer == "yes":
                main()

            # Question 5
        # Question 5 being presented to the user

        sleep(2)
        answerFive = (str(input(
            "\nLevel Five ($15000):             How Many Ribs Are in a Human-body?\n                                 ----------------------------------\n                                 (a) 20                (b) 37\n                                 (c) 24                (d) 7\nAnswer: ")))

        # If statements

        if answerFive == "c":
            sleep(0.7)
            print(outputMessageGain.format(levelFive - moneyMade, levelFive))
            moneyMade = levelFive
            score += 1
        elif answerFive == "lifeline" and LifeLine > 0:
            LifeLine -= 1
            sleep(1)
            print("\nYou have used a lifeline, \nYou now have", LifeLine, " lifeline remaining")
            sleep(2)
            print("\nHint: It is an even number")
            sleep(3)
            answerFive = (str(input(
                "\nLevel Five ($15000):             How Many Ribs Are in a Human-body?\n                                 ----------------------------------\n                                 (a) 20                (b) 37\n                                 (c) 24                (d) 7\nAnswer: ")))
            if answerFive == "c":
                sleep(0.7)
                print(outputMessageGain.format(levelFive - moneyMade, levelFive))
                moneyMade = levelFive
                score += 1
            elif answerFive == "lifeline" and LifeLine > 0:
                LifeLine = LifeLine - 1
                sleep(1)
                print("\nYou have used a lifeline, \nYou now have", LifeLine, " lifeline remaining")
                sleep(2)
                print("\nHint: It is divisibile by 6")
                sleep(3)
                answerFive = (str(input(
                    "\nLevel Five ($15000):             How Many Ribs Are in a Human-body?\n                                 ----------------------------------\n                                 (a) 20                (b) 37\n                                 (c) 24                (d) 7\nAnswer: ")))
                if answerFive == "c":
                    sleep(0.7)
                    print(outputMessageGain.format(levelFive - moneyMade, levelFive))
                    moneyMade = levelFive
                    score += 1
                elif answerFive != "c":
                    sleep(0.7)
                    print("\nSorry", name, "! You selected the wrong answer!")
                    lives = lives - 1
            elif answerFive != "c":
                sleep(0.7)
                print("\nSorry", name, "! You selected the wrong answer!")
                lives = lives - 1

        elif answerFive != "c":
            sleep(0.7)
            print("\nSorry", name, "! You selected the wrong answer!")
            lives = lives - 1

        # Lives and lifelines remaining

        sleep(1)
        print("\nYou have", lives, "lives remaining")
        sleep(0.7)
        print("You have", LifeLine, "lifeline remaining")

        # If user runs out of lives

        if lives < 0:
            sleep(0.7)
            print("\nYou got", score, "out of 10 correct!")
            sleep(1)
            answer = input("\nYou ran out of lives! Play again? Enter yes/no: ")
            if answer == "no":
                break
            if answer == "yes":
                main()

        # Question 6
        # Question 6 being presented to the user

        sleep(2)
        answerSix = (str(input(
            "\nLevel Six ($30000):                   What is the Sum of Interior Angles in a Triangle?\n                                      -------------------------------------------------\n                                      (a) 360                  (b) 180\n                                      (c) 90                   (d) 45\nAnswer: ")))

        # If statements

        if answerSix == "b":
            sleep(0.7)
            print(outputMessageGain.format(levelSix - moneyMade, levelSix))
            moneyMade = levelSix
            score += 1
        elif answerSix == "lifeline" and LifeLine > 0:
            LifeLine -= 1
            sleep(1)
            print("\nYou have used a lifeline, \nYou now have", LifeLine, " lifeline remaining")
            sleep(2)
            print("\nHint: It is the degree of a straight line")
            sleep(3)
            answerSix = (str(input(
                "\nLevel Six ($30000):                   What is the Sum of Interior Angles in a Triangle?\n                                      -------------------------------------------------\n                                      (a) 360                  (b) 180\n                                      (c) 90                   (d) 45\nAnswer: ")))
            if answerSix == "b":
                sleep(0.7)
                print(outputMessageGain.format(levelSix - moneyMade, levelSix))
                moneyMade = levelSix
                score += 1
            elif answerSix == "lifeline" and LifeLine > 0:
                LifeLine = LifeLine - 1
                sleep(1)
                print("\nYou have used a lifeline, \nYou now have", LifeLine, " lifeline remaining")
                sleep(2)
                print("\nHint: 360/2 ")
                sleep(3)
                answerSix = (str(input(
                    "\nLevel Six ($30000):                   What is the Sum of Interior Angles in a Triangle?\n                                      -------------------------------------------------\n                                      (a) 360                  (b) 180\n                                      (c) 90                   (d) 45\nAnswer: ")))
                if answerSix == "b":
                    sleep(0.7)
                    print(outputMessageGain.format(levelSix - moneyMade, levelSix))
                    moneyMade = levelSix
                    score += 1
                elif answerSix != "b":
                    sleep(0.7)
                    print("\nSorry", name, "! You selected the wrong answer!")
                    lives = lives - 1
            elif answerSix != "b":
                sleep(0.7)
                print("\nSorry", name, "! You selected the wrong answer!")
                lives = lives - 1

        elif answerSix != "b":
            sleep(0.7)
            print("\nSorry", name, "! You selected the wrong answer!")
            lives = lives - 1

        # Lives and lifeline remaining

        sleep(1)
        print("\nYou have", lives, "lives remaining")
        sleep(0.7)
        print("You have", LifeLine, "lifeline remaining")

        # If user runs out lives

        if lives < 0:
            sleep(0.7)
            print("\nYou got", score, "out of 10 correct!")
            sleep(1)
            answer = input("\nYou ran out of lives! Play again? Enter yes/no: ")
            if answer == "no":
                break
            if answer == "yes":
                main()

        # Question 7
        # Question 7 being presented to user

        sleep(2)
        answerSeven = (str(input(
            "\nLevel Seven ($60000):           Who is The Owner/Founder of Amazon?\n                                -----------------------------------\n                                (a) Jeff Bezos         (b) Elon Musk\n                                (c) Bill Gates         (d) Mark Zuckerberg\nAnswer: ")))

        # If statements

        if answerSeven == "a":
            sleep(0.7)
            print(outputMessageGain.format(levelSeven - moneyMade, levelSeven))
            moneyMade = levelSeven
            score += 1
        elif answerSeven == "lifeline" and LifeLine > 0:
            LifeLine -= 1
            sleep(1)
            print("\nYou have used a lifeline, \nYou now have", LifeLine, " lifeline remaining")
            sleep(2)
            print("\nHint: Elon Musk = Tesla, Bill Gates = Microsoft")
            sleep(3)
            answerSeven = (str(input(
                "\nLevel Seven ($60000):           Who is The Owner/Founder of Amazon?\n                                -----------------------------------\n                                (a) Jeff Bezos         (b) Elon Musk\n                                (c) Bill Gates         (d) Mark Zuckerberg\nAnswer: ")))
            if answerSeven == "a":
                sleep(0.7)
                print(outputMessageGain.format(levelSeven - moneyMade, levelSeven))
                moneyMade = levelSeven
                score += 1
            elif answerSeven == "lifeline" and LifeLine > 0:
                LifeLine = LifeLine - 1
                sleep(1)
                print("\nYou have used a lifeline, \nYou now have", LifeLine, " lifeline remaining")
                sleep(2)
                print("\nHint: Mark Zuckerberg is the founder of Facebook")
                sleep(3)
                answerSeven = (str(input(
                    "\nLevel Seven ($60000):           Who is The Owner/Founder of Amazon?\n                                -----------------------------------\n                                (a) Jeff Bezos         (b) Elon Musk\n                                (c) Bill Gates         (d) Mark Zuckerberg\nAnswer: ")))
                if answerSeven == "a":
                    sleep(0.7)
                    print(outputMessageGain.format(levelSeven - moneyMade, levelSeven))
                    moneyMade = levelSeven
                    score += 1
                elif answerSeven != "a":
                    sleep(0.7)
                    print("\nSorry", name, "! You selected the wrong answer!")
                    lives = lives - 1
            elif answerSeven != "a":
                sleep(0.7)
                print("\nSorry", name, "! You selected the wrong answer!")
                lives = lives - 1

        elif answerSeven != "a":
            sleep(0.7)
            print("\nSorry", name, "! You selected the wrong answer!")
            lives = lives - 1

        # Lives and lifelines remaining

        sleep(1)
        print("\nYou have", lives, "lives remaining")
        sleep(0.7)
        print("You have", LifeLine, "lifeline remaining")

        # If user runs out of lives

        if lives < 0:
            sleep(0.7)
            print("\nYou got", score, "out of 10 correct!")
            sleep(1)
            answer = input("\nYou ran out of lives! Play again? Enter yes/no: ")
            if answer == "no":
                break
            if answer == "yes":
                main()

        # Question 8
        # Question 8 being presented to user

        sleep(2)
        answerEight = (str(input(
            "\nLevel Eight ($100000):              What Country Invented Tea?\n                                    --------------------------\n                                    (a) China         (b) India\n                                    (c) Italy         (d) Brazil\nAnswer: ")))

        # If statements

        if answerEight == "a":
            sleep(0.7)
            print(outputMessageGain.format(levelEight - moneyMade, levelEight))
            moneyMade = levelEight
            score += 1
        elif answerEight == "lifeline" and LifeLine > 0:
            LifeLine -= 1
            sleep(1)
            print("\nYou have used a lifeline, \nYou now have", LifeLine, " lifeline remaining")
            sleep(2)
            print("\nHint: It is located in Asia")
            sleep(3)
            answerEight = (str(input(
                "\nLevel Eight ($100000):              What Country Invented Tea?\n                                    --------------------------\n                                    (a) China         (b) India\n                                    (c) Italy         (d) Brazil\nAnswer: ")))
            if answerEight == "a":
                sleep(0.7)
                print(outputMessageGain.format(levelEight - moneyMade, levelEight))
                moneyMade = levelEight
                score += 1
            elif answerEight == "lifeline" and LifeLine > 0:
                LifeLine = LifeLine - 1
                sleep(1)
                print("\nYou have used a lifeline, \nYou now have", LifeLine, " lifeline remaining")
                sleep(2)
                print("\nHint: It is beside India ")
                sleep(3)
                answerEight = (str(input(
                    "\nLevel Eight ($100000):              What Country Invented Tea?\n                                    --------------------------\n                                    (a) China         (b) India\n                                    (c) Italy         (d) Brazil\nAnswer: ")))
                if answerEight == "a":
                    sleep(0.7)
                    print(outputMessageGain.format(levelEight - moneyMade, levelEight))
                    moneyMade = levelEight
                    score += 1
                elif answerEight != "a":
                    sleep(0.7)
                    print("\nSorry", name, "! You selected the wrong answer!")
                    lives = lives - 1
            elif answerEight != "a":
                sleep(0.7)
                print("\nSorry", name, "! You selected the wrong answer!")
                lives = lives - 1

        elif answerEight != "a":
            sleep(0.7)
            print("\nSorry", name, "! You selected the wrong answer!")
            lives = lives - 1

        # Lives and lifelines remaining

        sleep(1)
        print("\nYou have", lives, "lives remaining")
        sleep(0.7)
        print("You have", LifeLine, "lifeline remaining")

        # If user runs out of lives

        if lives < 0:
            sleep(0.7)
            print("\nYou got", score, "out of 10 correct!")
            sleep(1)
            answer = input("\nYou ran out of lives! Play again? Enter yes/no: ")
            if answer == "no":
                break
            if answer == "yes":
                main()

        # Question 9
        # Question 9 being presented to user

        sleep(2)
        answerNine = (str(input(
            "\nLevel Nine ($500000):            What is Usain Bolt's 100m Record Time?\n                                 --------------------------------------\n                                 (a) 10.2s             (b) 9.62s\n                                 (c) 9.58s             (d) 10.18s\nAnswer: ")))

        # If statements

        if answerNine == "c":
            sleep(0.7)
            print(outputMessageGain.format(levelNine - moneyMade, levelNine))
            moneyMade = levelNine
            score += 1
        elif answerNine == "lifeline" and LifeLine > 0:
            LifeLine -= 1
            sleep(1)
            print("\nYou have used a lifeline, \nYou now have", LifeLine, " lifeline remaining")
            sleep(2)
            print("\nHint: It is less than 10s")
            sleep(3)
            answerNine = (str(input(
                "\nLevel Nine ($500000):            What is Usain Bolt's 100m Record Time?\n                                 --------------------------------------\n                                 (a) 10.2s             (b) 9.62s\n                                 (c) 9.58s             (d) 10.18s\nAnswer: ")))
            if answerNine == "c":
                sleep(0.7)
                print(outputMessageGain.format(levelNine - moneyMade, levelNine))
                moneyMade = levelNine
                score += 1
            elif answerNine == "lifeline" and LifeLine > 0:
                LifeLine = LifeLine - 1
                sleep(1)
                print("\nYou have used a lifeline, \nYou now have", LifeLine, " lifeline remaining")
                sleep(2)
                print("\nHint: It is the lowest time from the options ")
                sleep(3)
                answerNine = (str(input(
                    "\nLevel Nine ($500000):            What is Usain Bolt's 100m Record Time?\n                                 --------------------------------------\n                                 (a) 10.2s             (b) 9.62s\n                                 (c) 9.58s             (d) 10.18s\nAnswer: ")))
                if answerNine == "c":
                    sleep(0.7)
                    print(outputMessageGain.format(levelNine - moneyMade, levelNine))
                    moneyMade = levelNine
                    score += 1
                elif answerNine != "c":
                    sleep(0.7)
                    print("\nSorry", name, "! You selected the wrong answer!")
                    lives = lives - 1
            elif answerNine != "c":
                sleep(0.7)
                print("\nSorry", name, "! You selected the wrong answer!")
                lives = lives - 1

        elif answerNine != "c":
            sleep(0.7)
            print("\nSorry", name, "! You selected the wrong answer!")
            lives = lives - 1

        # Lives and lifelines remaining

        sleep(1)
        print("\nYou have", lives, "lives remaining")
        sleep(0.7)
        print("You have", LifeLine, "lifeline remaining")

        # If user runs out of lives

        if lives < 0:
            sleep(0.7)
            print("\nYou got", score, "out of 10 correct!")
            sleep(1)
            answer = input("\nYou ran out of lives! Play again? Enter yes/no: ")
            if answer == "no":
                break
            if answer == "yes":
                main()

        # Question 10
        # Question 10 being presented to user

        sleep(2)
        answerTen = (str(input(
            "\nLevel Ten ($1000000):             When Was Queen Elizabeth II Born?\n                                  ---------------------------------\n                                  (a) 1968             (b) 1942\n                                  (c) 1931             (d) 1926\nAnswer: ")))

        # If statements

        if answerTen == "d":
            sleep(0.7)
            print(outputMessageGain.format(levelTen - moneyMade, levelTen))
            moneyMade = levelTen
            score += 1
        elif answerTen == "lifeline" and LifeLine > 0:
            LifeLine -= 1
            sleep(1)
            print("\nYou have used a lifeline, \nYou now have", LifeLine, " lifeline remaining")
            sleep(2)
            print("\nHint: It is before 1942")
            sleep(3)
            answerTen = (str(input(
                "\nLevel Ten ($1000000):             When Was Queen Elizabeth II Born?\n                                  ---------------------------------\n                                  (a) 1968             (b) 1942\n                                  (c) 1931             (d) 1926\nAnswer: ")))
            if answerTen == "d":
                sleep(0.7)
                print(outputMessageGain.format(levelTen - moneyMade, levelTen))
                moneyMade = levelTen
                score += 1
            elif answerTen == "lifeline" and LifeLine > 0:
                LifeLine = LifeLine - 1
                sleep(1)
                print("\nYou have used a lifeline, \nYou now have", LifeLine, " lifeline remaining")
                sleep(2)
                print("\nHint: It is an even numbered year ")
                sleep(3)
                answerTen = (str(input(
                    "\nLevel Ten ($1000000):             When Was Queen Elizabeth II Born?\n                                  ---------------------------------\n                                  (a) 1968             (b) 1942\n                                  (c) 1931             (d) 1926\nAnswer: ")))
                if answerTen == "d":
                    sleep(0.7)
                    print(outputMessageGain.format(levelTen - moneyMade, levelTen))
                    moneyMade = levelTen
                    score += 1
                elif answerTen != "d":
                    sleep(0.7)
                    print("\\nSorry", name, "! You selected the wrong answer!")
                    lives = lives - 1
            elif answerTen != "d":
                sleep(0.7)
                print("\nSorry", name, "! You selected the wrong answer!")
                lives = lives - 1

        elif answerTen != "d":
            sleep(0.7)
            print("\nSorry", name, "! You selected the wrong answer!")
            lives = lives - 1

        # Lives and lifelines remaining

        sleep(1)
        print("\nYou have", lives, "lives remaining")
        sleep(0.7)
        print("You have", LifeLine, "lifeline remaining")

        # If user runs out of lives

        if lives < 0:
            sleep(0.7)
            print("\nYou got", score, "out of 10 correct!")
            sleep(1)
            answer = input("\nYou ran out of lives! Play again? Enter yes/no: ")
            if answer == "no":
                break
            if answer == "yes":
                main()

        # If user has managed to complete all questions, so they still have <= 0 lives, it will show the money made, their score and will ask if they want to play again

        if lives >= 0:
            sleep(0.7)
            print("\nYou got", score, "out of 10 correct!")
            sleep(1)
            print("You won $", moneyMade, "!")
            sleep(1)
            answer = input("\nPlay again? Enter yes/no: ")
            if answer == "no":
                break
            if answer == "yes":
                main()

    # The 'break' of the loop, that was mentioned earlier (Tells the user thank you for playing)

    print("\nGame Over!", outputMessageLoss)
    sleep(0.7)
    print("*applause*")


main()