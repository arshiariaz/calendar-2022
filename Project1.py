# File: Project1.py
# Student: Arshia Riaz
# 
# Date Created: 10/04/2021
# Date Last Modified: 10/08/2021
# Description of Program: This program displays the days of the inputted month for the year 2022


#input month number
m = int(input("Enter the number of a month [1..12]: "))

#given user enters value not corresponding to a month
while (m > 12) or (m < 1):
    print("Month must be between 1 and 12. Try again!")
    m = int(input("Enter the number of a month [1..12]: "))
    
#return month's name
if (m == 1):
    m = "January"
    t = 6
    d = 31
elif (m == 2):
    m = "February"
    t = 2
    d = 28
elif (m == 3):
    m = "March"
    t = 2
    d = 31
elif (m == 4):
    m = "April"
    t = 5
    d = 30
elif (m == 5):
    m = "May"
    t = 0
    d = 31
elif (m == 6):
    m = "June"
    t = 3
    d = 30
elif (m == 7):
    m = "July"
    t = 5
    d = 31
elif (m == 8):
    m = "August"
    t = 1
    d = 31
elif (m == 9):
    m = "September"
    t = 4
    d = 30
elif (m == 10):
    m = "October"
    t = 6
    d = 31
elif (m == 11):
    m = "November"
    t = 2
    d = 30
elif (m == 12):
    m = "December"
    t = 4
    d = 31

#displays month's days
print()
print("   ", m, " 2022")
print("Su Mo Tu We Th Fr Sa ")
for i in range(0, t):
    print(format(" ", "3s"), end='')
for i in range(1,d + 1):
    if i < 10:
        print(format(i, "2d"), end=' ')
    else:
        print(format(i, "2d"), end=' ')
    if (i + t) % 7 == 0:
        print()
if (m == "January") or (m == "February") or (m == "March") or (m == "May") or (m == "June") or (m == "July") or (m == "August") or (m == "September") or (m == "October") or (m == "November"):
    print("\n")
if (m == "April") or (m == "December"):
    print("\t")
