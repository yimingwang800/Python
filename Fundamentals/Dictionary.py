car_dict = {
    #"Key" : "Value"
    "brand" : "Volkswagon",
    "model": "Tiguan",
    "year": 2019
}

print(car_dict)
print(len(car_dict))         #The size of the dictionary
print(car_dict["model"])     #Try the key doesn't exist (ex: add 1)
print(car_dict.get("model")) #Try the key doesn't exist
print(car_dict.get("model1")) #Says "None"
if "model" in car_dict:
    print("Yes, 'model' is in the car_dict dictionary")

# Add seats to car_dict, if "seats" does not exist
car_dict["seats"] = 7

# Moduiy the year if "year" does exist
car_dict["year"] = 2018

# Remove specific item
car_dict.pop("model")
#del car_dict["model"]

# Remove the last inserted item
car_dict.popitem()

# Delete dictionary completely
car_dict.clear()
#del car_dict

for key in car_dict:    #Or
    print(key)
    print(car_dict[key])    #Or
    print("Key: {}, Value: {}".format(key, car_dict[key]))

for value in car_dict.values():    #Don't know what key it is
    print(value)

for key, value in car_dict.items():
    print(key, value)   #Or
    print(f"Key: {key}, Value: {value}")

#Just pointer, change new_car_dict will change car_dict
new_car_dict = car_dict

# Two different list that will have the same data
new_car_dict = car_dict.copy()

print(car_dict)

# Sort the dictionary
for key in sorted(car_dict):
    print(key)
    print(car_dict[key])



