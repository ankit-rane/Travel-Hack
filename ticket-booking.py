global f
f = 0


# this t_movie function is used to select movie name
def t_movie():
    global f
    f = f + 1
    print("which country do you want to visit?")
    print("1. India ")
    print("2 The United States of America ")
    print("3. The United Kingdom")
    print("4 Back")
    movie = int(input("choose your country: "))
    if movie == 4:
        center()
        theater()
        return 0
    if f == 1:
        theater()


# this theater function used to select screen
def theater():
    print("which transport do you wish to go by: ")
    print("1. Flight")
    print("2. Cruise")
    a = int(input("choose your screen: "))
    ticket = int(input("number of ticket do you want?: "))
    timing(a)


# this timing function used to select timing for movie
def timing(a):
    time1 = {
        "1": "10.00",
        "2": "1.10",
        "3": "4.20",
        "4": "7.30"
    }
    time2 = {
        "1": "10.15",
        "2": "1.25",
        "3": "4.35",
        "4": "7.45"
    }
    if a == 1:
        print("choose your time:")
        print(time1)
        t = input("select your time:")
        x = time1[t]
        print("successfull!, enjoy the journey " + x)
    elif a == 2:
        print("choose your time:")
        print(time2)
        t = input("select your time:")
        x = time2[t]
        print("successfull!, enjoy the journey " + x)
    return 0


def movie(theater):
    if theater == 1:
        t_movie()
    elif theater == 2:
        t_movie()
    elif theater == 3:
        t_movie()
    elif theater == 4:
        city()
    else:
        print("wrong choice")


def center():
    print("which flight do you wish to travel with? ")
    print("1. Jet airways")
    print("2. Qatar")
    print("3. Lufthansa")
    print("4. Back")
    a = int(input("choose your option: "))
    movie(a)
    return 0


# this function is used to select city
def city():
    print("Hi welcome to travel ticket booking: ")
    print("where you want to travel?:")
    print("1. Mumbai")
    print("2. New York")
    print("3. London")
    place = int(input("choose your option: "))
    if place == 1:
        center()
    elif place == 2:
        center()
    elif place == 3:
        center()
    else:
        print("wrong choice")