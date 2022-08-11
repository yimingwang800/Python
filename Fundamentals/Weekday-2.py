my_int = input("Enter integer: ")
date = int(input())
day =  date % 7
if day == 0 :       
    print("The {} day is Sunday".format(date))
elif day == 1:       
    print("The {} day is Monday".format(date))
elif day == 2:       
    print("The {} day is Tuesday".format(date))
elif day == 3:       
    print("The {} day is Wednesday".format(date))
elif day == 4:       
    print("The {} day is Thursday".format(date))
elif day == 5:       
    print("The {} day is Friday".format(date))
else:       
    print("The {} day is Saturday".format(date))