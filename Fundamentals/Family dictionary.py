my_family = {
    "Mom": {
        "Name": "Rock",
        "Birth_Year": 1900,
    },
    "Dad": {
        "Name": "Paper",
        "Birth_year": 1000
    },
    "Sister":{
        "Name": "Scissors",
        "birth_year": 2000
    }
}


for id, info in my_family.items():
    print(id)
    for key in info:
        print(" " + key + ':', info[key])
    print()

