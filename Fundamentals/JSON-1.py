# [] = List, {} = Dictionary
peoples = [
    {
        "Name": "Rock",
        "City": "Ottawa",
        "Age": "1"
    },
    {
        "Name": "Paper",
        "City": "Ottawa",
        "Age": "100"
    },
    {
        "Name": "Scissors",
        "City": "Ottawa",
        "Age": "1000" 
    }
]

for peoples in peoples:
    for key in peoples:
        print(key + ':', peoples[key])
    print()