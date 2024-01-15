# importing random module
import math
import random
from numpy import random

randomList=[]
# repeat 50 times
for i in range(50):
   # generating a random number in the range 1 to 200
   r=random.randint(1,200)
   # check if the generated random number is not in the randomList
   if r not in randomList:
      # appending the random number to the list, if the condition is true
      randomList.append(r)
# printing the random numbers list
#print(randomList)

#sort list in ascending order
randomList.sort()
print("The size of the random list is: ",len(randomList))
print("The random list is: ")
print(randomList)

x = random.randint(len(randomList))
y= int(randomList[x])
print("Please find if",y,"is in the list")
low_index=int(0)
high_index=int(len(randomList)-1)
middle_index= int((low_index+high_index)/2)
   
while(low_index<high_index):
   if randomList[middle_index]>y:
      high_index=middle_index
      middle_index= int((low_index+high_index)/2)
   elif randomList[middle_index]<y:
      low_index=middle_index
      middle_index= int((low_index+high_index)/2)
   else:
      print("Yes", y,"is in the list and it's in postion",middle_index+1)
      break

print("the total number of operation is",math.ceil((math.log(len(randomList),2))))

