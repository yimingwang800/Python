import json
str_json =  '[{"name": "John", "city": "Ottawa", "age": 30}, {"name": "Smith", "city": "Toronto", "age": 31}]'
print(type(str_json))
print(str_json)
data = json.loads(str_json) #JSON load frok string
print(type(data))
print(data)
print(data[0]["age"])
print(data[1]["city"])

