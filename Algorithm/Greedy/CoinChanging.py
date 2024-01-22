amount = int(input("Please enter the amount:"))

num_of_25 = int(amount/25)
num_of_10 = int((amount-num_of_25*25)/10)
num_of_5 = int((amount-num_of_25*25- num_of_10*10)/5)
num_of_1 = int(amount-num_of_25*25- num_of_10*10 - num_of_5*5)

print("25 Cent  ",num_of_25)
print("10 Cent  ",num_of_10)
print("5 Cent   ",num_of_5)
print("1 Cent   ",num_of_1)
