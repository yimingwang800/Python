import math
#list = [4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30]
list = [3, 8, 11, 12, 13, 16, 17, 18, 26, 28, 38, 42, 47, 55, 58, 61, 65, 67, 68, 77, 81, 82, 85, 93,
         95, 101, 111, 122, 124, 131, 133, 148, 149, 150, 156, 163, 165, 168, 169, 173, 180, 194, 195, 197, 200]
y=3
count = 0
low_index=int(0)
high_index=int(len(list)-1)
middle_index= int((low_index+high_index)/2)
while(low_index<high_index):
    count+=1
    if list[middle_index]>y:
        high_index=middle_index
        middle_index= int((low_index+high_index)/2)
    elif list[middle_index]<y:
        low_index=middle_index
        middle_index= int((low_index+high_index)/2)
    else:
        print( y,"is in the list and it's in postion",middle_index)
        break

print("The total number of operation is",math.ceil((math.log(len(list),2))))
print("The total number of actual operation is", count)