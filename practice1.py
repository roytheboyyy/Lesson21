from datetime import date , time , datetime
date = int(input("enter a month number"))
if date < 1 or date > 12:
    print("invalid month number")

elif date == 1:
    print("january")
elif date == 2:
    print("february")
elif date == 3:
    print("march")
elif date == 4:
    print("april")
elif date == 5:
    print("may")
elif date == 6:
    print("june")
elif date == 7:
    print("july")
elif date == 8:
    print("august")
elif date == 9:
    print("september")
elif date == 10:
    print("october")
elif date == 11:
    print("november")
elif date == 12:   
    print("december")