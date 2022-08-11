my_int = input("Enter integer: ")
number = int(input())
day = number % 7
if day == 0 :        
    print("Sunday")
elif day == 1:       
    print("Monday")
elif day == 2:       
    print("Tuesday")
elif day == 3:       
    print("Wednsday")
elif day == 4:       
    print("Thursday")
elif day == 5:       
    print("Friday")
else:       
    print("Saturday")