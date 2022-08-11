number = int(input())
num_to_str = str(number)
length = len(num_to_str)
for i in range(length, 0, -1) :
    print(int(number%(10**i)/10**(i-1)))

