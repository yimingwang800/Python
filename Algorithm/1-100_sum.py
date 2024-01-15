#list=[]
# for i in range(1, 101):
#     list.append(i)
# print(list)

#sum=((list[0]+list[99])*100/2)
#print(sum)

#O(1)
# sum=(1+100)*100/2
# print(sum)

#O(n)
sum = 0
for i in range(1, 101):
    sum = sum + i
print(sum)
