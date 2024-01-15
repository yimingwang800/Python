import math
# number = int(input())
# prime_indicator = 0
# for i in range(2, number-1):
#     if number%i == 0:
#         prime_indicator = 1
#         break

# if prime_indicator == 1:
#     print(number,"is not a prime number")
# else:
#     print(number,"is a prime number")
# #O(n)

number = int(input())
prime_indicator = 0
for i in range(2, int(math.sqrt(number))+1):
    if number%i == 0:
        prime_indicator = 1
        break

if prime_indicator == 1:
    print(number,"is not a prime number")
else:
    print(number,"is a prime number")
#O(sqrt(n))
    
    

