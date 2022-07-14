fruit_list = ["Watermelon", "Dragon Fruit", "Apple", "Blackberry"]
print(fruit_list)
print(fruit_list[1])    #Start at 0
print(fruit_list[-1])   #-1 = last one, -2 = second last
print(fruit_list[0:2])  #Range of the list, items from index 0 to 2, index 2 item is NOT included
print(len(fruit_list))  #Size of the list, how many elemenst in the array

other_list = ["Apple", "Banana", "Cherry", 1, 10, "a", 5.3]
if "Apple" in fruit_list:   #C++ use find function
    print("Yes, 'Apple' is is in the list!")

fruit_list.append("Orange")     #Add fruit to fruit_list from end
print(fruit_list)

fruit_list.insert(1, "Pear")     #Add fruit to fruit_list from middle by index
print(fruit_list)

fruit_list[1] = "Blackcurrant"   #Modify item
print(fruit_list)


#fruit_list.remove("Orange")     #Remove specific item
#print(fruit_list)
#Remove the specified index, or the last item if index is not specified
#fruit_list.pop()    #Remove the last element
#print(fruit_list)

#fruit_list.pop(1)    #Remove fruit_list[1]
#print(fruit_list)

#fruit_list.clear()   #Empties the list
#print(fruit_list)


#Iterate list by index
for i in range(len(fruit_list)):    #For example: 5
    print(fruit_list[i])            # i = 0, 1, 2, 3, 4

#Iterate list by index
for fruit in fruit_list:    #Variable: fruit
    print(fruit)            #The value is in the variable fruit

#Just pointer, change new_fruit_list_ will change fruit_list
new_fruit_list = fruit_list
new_fruit_list[0] = "banana"    #fruit_list[0] is "banana" now
print(fruit_list)

#Two different list have same data (copy info to another list)
newest_fruit_list = fruit_list.copy()
newest_fruit_list[0] = "strawberry"
print(newest_fruit_list)

#Sort the list, the list will change the order
list_1 = [8, 2, 6, 12, 10]
#list_1.sort()
#print(list_1)

#Make a new list that is sorted
new_list = sorted(list_1)
print(list_1)
print(new_list)

#Join two list with different data type
list_2 = ["A", "B", "C", "D", "E"]
list_3 = [1, 2, 3, 4, 5]

list_4 = list_2 + list_3
print(list_4)

list_2.extend(list_3)
print(list_2)

#Append
list_2 = ["A", "B", "C", "D", "E"]
list_3 = [1, 2, 3, 4, 5]
list_2.append(list_3)
print(list_2)

#Append a list to list
list_2 = ["A", "B", "C", "D", "E", [1, 2, 3, 4, 5]]
list_2.append(list_3)
print(list_2)

#Tuple - Immutable List (cannot modify)
fruit_tuple = ("apple", "banana", "cherry") #same as the other code
print(fruit_tuple)

#Set - Unordered collections of unique elements (no repeating an element)
fruit_set = {"apple", "cherry", "banana"}
fruit_set.add("orange")
fruit_set.add("apple")
print(fruit_set)