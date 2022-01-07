# Date: December 19th, 2021
# Programmer: Amit Singh Mehmi
#
# Description: This is a application for runners! It calculates splits, has videos and a running game!
#


# Module import
from PIL import ImageTk
import PIL.Image
from tkinter import *
import pygame
import time

def welcomewindow():

    # Welcome window size, window title, window mini icon that's top left
    welcome_window = Tk()
    welcome_window.geometry("800x500")
    welcome_window.title("Welcome to STEMINA!")
    welcome_window.configure(bg="grey")
    welcome_window.iconbitmap("steminalogo_Cvd_icon.ico")
    pygame.mixer.init()

    # STEMINA logos in Welcome Window
    global welcome_window_logo
    welcome_window_logo = ImageTk.PhotoImage(PIL.Image.open("steminalogo_Cvd_icon.ico"))
    welcome_window_logoimage = Label(image=welcome_window_logo)
    welcome_window_logoimage.place(relx=0.18, rely=0.010)

    global welcome_window_logo2
    welcome_window_logo2 = ImageTk.PhotoImage(PIL.Image.open("steminalogo_Cvd_icon.ico"))
    welcome_window_logo2image = Label(image=welcome_window_logo2)
    welcome_window_logo2image.place(relx=0.74, rely=0.010)

    # Welcome window main title
    welcome_label = Label(welcome_window, text="  Welcome to STEMINA!  ", font="times 25", relief="solid", bg="#4B0082", fg="White").pack(pady=10)

    # Please enter your name text
    enter_name = Label(welcome_window, text="↓ Please Enter Your Name Below ↓", bg="#4B0082", fg="White", relief="solid").place(relx=0.38, rely=0.18)

    # Enter your name input
    input = Entry(welcome_window, width=50, bg="#4B0082", fg="White", borderwidth=5, font="Times 14")
    input.place(relx=0.2, rely=0.25)
    input.insert(0, "")

    # Submission Process
    def submission():
        global user_name
        user_name = input.get()

    submission()

    # Submit button
    submit_button = Button(welcome_window, text="Submit Name", font="times 15", command= submission, bg="#4B0082", fg="White").place(relx=0.42, rely=0.35)

    # Continue statement for welcome menu
    def continuetomenu():
        wordcount = len(user_name)
        if wordcount > 0:
            welcome_window.destroy()
            pygame.mixer.music.load("Work Out Instrumental-J.Cole HQ.mp3")
            pygame.mixer.music.play()
            mainmenu()
        else:
            error = Label(welcome_window, text="Please Enter a Name and Click Submit!", bg="#4B0082", fg="yellow").pack(side=BOTTOM)
            pygame.mixer.music.load("please_enter_your_name.mp3")
            pygame.mixer.music.play()

    # Continue button
    continuebutton = Button(welcome_window, text="Click to Continue", font="Times 18", bg="#4B0082", fg="White", command=continuetomenu).place(relx=0.38, rely=0.5)


def mainmenu():

    global mainmenu_window
    # Main Menu window size, window title, window mini icon that's top left, main menu music
    mainmenu_window = Tk()
    mainmenu_window.geometry("2000x500")
    mainmenu_window.title("STEMINA INTERFACE")
    mainmenu_window.configure(bg="grey")
    mainmenu_window.iconbitmap("steminalogo_Cvd_icon.ico")
    pygame.mixer.init()

    # ↓ IMAGES ↓

    # Track image in the background in Main Menu
    global track_pic
    track_pic = ImageTk.PhotoImage(PIL.Image.open("output-onlinepngtools (4).png"))
    track_picimage = Label(image=track_pic)
    track_picimage.place(relx=0, rely=0)

    # Image on top of video button in Main Menu
    global video_pic
    video_pic = ImageTk.PhotoImage(PIL.Image.open("videospic.png"))
    video_picimage = Label(image=video_pic)
    video_picimage.place(relx=0.0855, rely=0.3)

    # Image on top of splits calculator button in Main Menu
    global splits_pic
    splits_pic = ImageTk.PhotoImage(PIL.Image.open("splitspic.png"))
    splits_picimage = Label(image=splits_pic)
    splits_picimage.place(relx=0.81, rely=0.3)

    # Image on top of running game button in Main Menu
    global running_game_pic
    running_game_pic = ImageTk.PhotoImage(PIL.Image.open("runninggamepic.png"))
    running_game_picimage = Label(image=running_game_pic)
    running_game_picimage.place(relx=0.46, rely=0.3)

    # Main Menu logo beside title left side
    global menu_logo
    menu_logo = ImageTk.PhotoImage(PIL.Image.open("steminalogo_Cvd_icon.ico"))
    menu_logoimage = Label(image=menu_logo)
    menu_logoimage.place(relx=0.35, rely=0.010)

    # Main Menu logo beside title right side
    global menu_logo2
    menu_logo2 = ImageTk.PhotoImage(PIL.Image.open("steminalogo_Cvd_icon.ico"))
    menu_logoimage2 = Label(image=menu_logo2)
    menu_logoimage2.place(relx=0.62, rely=0.010)

    # Clock, Date, and Welcome label underneath title
    def clockanddate():
        hour = time.strftime("%I")
        minute = time.strftime("%M")
        second = time.strftime("%S")
        date = time.strftime("%x")
        am_pm = time.strftime("%p")

        clock.config(text=hour + ":" + minute + ":" + second + am_pm)
        clock.after(1000, clockanddate)

        dmy.config(text=date)

    def update():
        clock.config(text="New Text")

    clock = Label(mainmenu_window, text="", fg="#4B0082")
    clock.place(relx=0.545, rely=0.145)

    dmy = Label(mainmenu_window, text="", fg="#4B0082")
    dmy.place(relx=0.58, rely=0.145)

    welcome_name = "Welcome to STEMINA Interface, " + user_name + "!"
    welcome_label = Label(text=welcome_name, fg="#4B0082").place(relx=0.39, rely=0.145)

    clockanddate()


    def splitscalculator():

        pygame.mixer.music.pause()
        global splitscalculator_window
        splitscalculator_window = Tk()
        splitscalculator_window.geometry("800x500")
        splitscalculator_window.config(bg="grey")
        splitscalculator_window.title("STEMINA Splits Calculator")
        splitscalculator_label = Label(splitscalculator_window, text="  Splits Calculator!  ", font="times 20",relief="solid", bg="#4B0082", fg="White").pack(pady=10)
        splitscalculator_window.iconbitmap("steminalogo_Cvd_icon.ico")

        runnning_event_label = Label(splitscalculator_window, text=" Event(m):  ", relief="solid", fg="yellow", bg="#4B0082").place(relx=0.15, rely=0.2)
        second_label = Label(splitscalculator_window, text="  Second(s):  ", relief="solid", fg="yellow", bg="#4B0082").place(relx=0.15, rely=0.3)
        minutes_label = Label(splitscalculator_window, text="  Minute(s):  ", relief="solid", fg="yellow", bg="#4B0082").place(relx=0.15, rely=0.4)
        hours_label = Label(splitscalculator_window, text="  Hour(s):  ", relief="solid", fg="yellow", bg="#4B0082").place(relx=0.15, rely=0.5)
        desired_splits_label = Label(splitscalculator_window, text="  Splits Every(m):  ", relief="solid", fg="yellow", bg="#4B0082").place(relx=0.15, rely=0.6)
        results_label =  Label(splitscalculator_window, text="  Results:  ", relief="solid", fg="yellow", bg="#4B0082").place(relx=0.15, rely=0.7)

        running_event = Entry(splitscalculator_window, width=35, bg="#4B0082", fg="white", borderwidth=5, font="times 10")
        running_event.place(relx=0.4, rely=0.2)
        running_event.insert(0, "")

        seconds = Entry(splitscalculator_window, width=35, bg="#4B0082", fg="white", borderwidth=5, font="times 10")
        seconds.place(relx=0.4, rely=0.3)
        seconds.insert(0, "")

        minutes = Entry(splitscalculator_window, width=35, bg="#4B0082", fg="white", borderwidth=5, font="times 10")
        minutes.place(relx=0.4, rely=0.4)
        minutes.insert(0, "")

        hours = Entry(splitscalculator_window, width=35, bg="#4B0082", fg="white", borderwidth=5, font="times 10")
        hours.place(relx=0.4, rely=0.5)
        hours.insert(0, "")

        desired_splits = Entry(splitscalculator_window, width=35, bg="#4B0082", fg="white", borderwidth=5, font="times 10")
        desired_splits.place(relx=0.4, rely=0.6)
        desired_splits.insert(0, "")

        def splitssubmission():
            global userseconds, userminutes, userhours, userevent, usersplits
            userevent = running_event.get()
            userseconds = seconds.get()
            userminutes = minutes.get()
            userhours = hours.get()
            usersplits = desired_splits.get()

            if userevent == "":
                userevent = 0
            else:
                userevent = int(userevent)

            if userseconds == "":
                userseconds = 0
            else:
                userseconds = int(userseconds)

            if userminutes == "":
                userminutes = 0
            else:
                userminutes = int(userminutes)

            if userhours == "":
                userhours = 0
            else:
                userhours = int(userhours)

            if usersplits == "":
                usersplits = 0
            else:
                usersplits = int(usersplits)

        def clear():
            running_event.delete(0, END)
            seconds.delete(0, END)
            minutes.delete(0, END)
            hours.delete(0, END)
            desired_splits.delete(0, END)
            result2.destroy()
            result.destroy()
            errorc.destroy()

        def splitscalculation():

            if userhours + userminutes + userseconds + usersplits + userevent == 0:
                global errorc
                errorc = Label(splitscalculator_window, text="Please Fill in Fields, Click Submit, then Get Results!", bg="#4B0082", fg="yellow")
                errorc.place(relx=0.34, rely=0.12)
                pygame.mixer.music.load("please_fill_fields.mp3")
                pygame.mixer.music.play()

            timeCalculation = (userminutes * 60) + userseconds + (userhours * 3600)
            distanceCalculation = timeCalculation / userevent
            splitsCalculation = distanceCalculation * usersplits

            if splitsCalculation >= 60 and splitsCalculation < 3600:
                splitsCalculationMinutes = int(splitsCalculation // 60)
                splitsCalculationSeconds = (splitsCalculation - 60 * splitsCalculationMinutes)
                splitsoverall = splitsCalculationMinutes, str("minutes"), (format(splitsCalculationSeconds, ".2f")) + str(" seconds")

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

            global result, result2
            result = Label(splitscalculator_window, bg="#4B0082", fg="white", borderwidth=5, text=" To run, " + str(userevent) + " meters in: " + str(userhours) + " hours " + str(userminutes) + " minutes " + str(userseconds) + " seconds ")
            result.place(relx=0.4, rely=0.7)
            result2 = Label(splitscalculator_window, bg="#4B0082", fg="white", borderwidth=5, text= " Your split every " + str(usersplits) + " meters should be in: " + str(splitsoverall))
            result2.place(relx=0.4, rely=0.75)

        def exitsplits():
            splitscalculator_window.destroy()
            pygame.mixer.music.load("Work Out Instrumental-J.Cole HQ.mp3")
            pygame.mixer.music.play()

        splits_submitbutton = Button(splitscalculator_window, text="Submit", font="Times 10", bg="#4B0082", fg="White", command=splitssubmission).place(relx=0.2, rely=0.9)
        get_splits = Button(splitscalculator_window, text="Get Results", font="Times 10", bg="#4B0082", fg="White", command=splitscalculation).place(relx=0.3, rely=0.9)
        button_clear = Button(splitscalculator_window, text="Clear", font="Times 10", bg="#4B0082", fg="White", command=clear).place(relx=0.427, rely=0.9)
        exit = Button(splitscalculator_window, text="Exit Calculator", font="Times 10", bg="#4B0082", fg="White", command=exitsplits).place(relx=0.5, rely=0.9)


    # Main Menu Buttons
    def mainmenubuttons():
        global stemina_label, splits_calculator, videos, game, mute, unmute
        stemina_label = Label(mainmenu_window, text="STEMINA INTERFACE", font="Times 32", relief="solid", fg="White", bg="#4B0082").pack(pady=10)
        splits_calculator = Button(mainmenu_window, text="Splits Calculator", font="Times 20", fg="Yellow", bg="#4B0082", command=splitscalculator).place(relx=0.9, rely=0.7, anchor=E)
        videos = Button(mainmenu_window, text="Videos", font="Times 20", fg="Yellow", bg="#4B0082").place(relx=0.1, rely=0.7, anchor=W)
        game = Button(mainmenu_window, text="Running Game", font="Times 20", fg="Yellow", bg="#4B0082").place(relx=0.5, rely=0.7, anchor=CENTER)
        mute = Button(mainmenu_window, text="Mute Music", font="Times 10", command=pygame.mixer.music.pause, fg="Yellow", bg="#4B0082").place(relx=1.0, rely=1.0, anchor=SE)
        unmute = Button(text="Unmute Music", font="Times 10", command=pygame.mixer.music.unpause, fg="Yellow", bg="#4B0082").place(relx=1.0, rely=0.945, anchor=SE)

    mainmenubuttons()


welcomewindow()
mainloop()
