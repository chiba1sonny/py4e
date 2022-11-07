# 3.1 Write a program to prompt the user for hours and rate per hour using
# input to compute gross pay. Pay the hourly rate for the hours up to 40 and
# 1.5 times the hourly rate for all hours worked above 40 hours. Use 45 hours
# and a rate of 10.50 per hour to test the program (the pay should be 498.75).
# You should use input to read a string and float() to convert the string to a
# number. Do not worry about error checking the user input - assume the user
# types numbers properly.

hrs = input("Input your working hours:")
hrs = float(hrs)

rate1 = input("Enter the rate by 40 hours: ")
rate1 = float(rate1)

times = input("Enter the number of times when above 40 hours:")
times = float(times)

rate2 = rate1*times

if hrs > 40:
    pay = 40*rate1+(hrs-40)*rate2
else:
    pay = hrs*rate1
print(pay)
