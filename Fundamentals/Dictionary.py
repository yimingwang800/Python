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
