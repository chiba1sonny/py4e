scr = input("Please Enter Your Score:")

try:
    scr = float(scr)
except:
    scr = -1

if scr >= 0.9:
    print("A")
elif scr >= 0.8:
    print("B")
elif scr >= 0.7:
    print("C")
elif scr >= 0.6:
    print("D")
else:
    print("F")
