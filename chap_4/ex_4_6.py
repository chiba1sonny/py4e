# 4.6 Write a program to prompt the user for hours and rate per hour using
# input to compute gross pay. Pay should be the normal rate for hours up to
# 40 and time-and-a-half for the hourly rate for all hours worked above 40
# hours. Put the logic to do the computation of pay in a function called
# computepay() and use the function to do the computation. The function
# should return a value. Use 45 hours and a rate of 10.50 per hour to test the
# program (the pay should be 498.75). You should use input to read a string
# and float() to convert the string to a number. Do not worry about error
# checking the user input unless you want to - you can assume the user types
# numbers properly. Do not name your variable sum or use the sum() function.
def computepay(hrs, rate1, times):
    if hrs <= 40:
        pay = hrs*rate1
    else:
        pay = 40*rate1+(hrs-40)*rate2
    return pay
hrs = input("Please Enter Your HOURS :")
hrs = float(hrs)
rate1 = input("Please Enter Your RATE :")
rate1 = float(rate1)
times = input("Please Enter the TIME, Which Should be 1.5 :")
times = float(times)
rate2 = rate1*times
payment = computepay(hrs, rate1, times)
print('Pay', payment)
