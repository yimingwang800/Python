data = {
    "Group 1":
    [
        {
            "Name": "Rock",
            "City": "Ottawa",
            "Age": "1"
        },
        {
            "Name": "Paper",
            "City": "Ottawa",
            "Age": "100"
        }
    ],
    "Group 2":
    [   
        {
            "Name": "Scissors",
            "City": "Ottawa",
            "Age": "1000" 
        }
    ]
}

for group, details in data.items():
    print(group + ":")
    for info in details:
        for key in info:
            print("  " + key + ':', info[key])
        print()
    print()