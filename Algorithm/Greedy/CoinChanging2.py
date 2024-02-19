number_of_values = []

def calculation_function():
    amount = int(input("Please enter the amount in cents:"))
    value_list = [10000, 5000, 2000, 1000, 500, 200, 100, 25, 10, 5, 1]

    i = 0
    while i in range(len(value_list)):
        if int(amount%value_list[i]) != 0:
            x = int (amount/value_list[i])
            number_of_values.append(x) 
            amount = amount-x*value_list[i]
            i+=1
        elif int(amount%value_list[i]) == 0:
            x = int (amount/value_list[i])
            number_of_values.append(x)  
            amount = amount-x*value_list[i]
            i+=1
            

calculation_function()
print("number of $100:     ", number_of_values[0])
print("number of $50:      ", number_of_values[1])
print("number of $20:      ", number_of_values[2])
print("number of $10:      ", number_of_values[3])
print("number of $5:       ", number_of_values[4])
print("number of $2:       ", number_of_values[5])
print("number of $1:       ", number_of_values[6])
print("number of 25 cents: ", number_of_values[7])
print("number of 10 cents: ", number_of_values[8])
print("number of 5 cents:  ", number_of_values[9])
print("number of 1 cents:  ", number_of_values[10])
