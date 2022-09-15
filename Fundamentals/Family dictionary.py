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

for member, details in my_family.items():
    print(member)
    for key in details:
        print(" " + key + ':', details[key])
    print()

