# list_2d = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9],
# ]
# print(list_2d)
# for num in list_2d:
#     for numbers in num:
#         print(numbers, end = " ")
#     print()


nested_dict = {
    'ground_1': {'1': 1, '2': 2, '3': 3}, 
    'ground_2': {'4': 4, '5': 5, '6': 6}, 
    'ground_3': {'7': 7, '8': 8, '9': 9}, 
}
# for key, value in nested_dict.items():
#     for name in value:
#         for number in name:
#             print(number, end = " ")
#     print()


json = {
    'data': [
        {'1': 1, '2': 2, '3': 3}, 
        {'4': 4, '5': 5, '6': 6}, 
        {'7': 7, '8': 8, '9': 9}
    ]
}
json = [
    {'1': 1, '2': 2, '3': 3}, 
    {'4': 4, '5': 5, '6': 6}, 
    {'7': 7, '8': 8, '9': 9},  
]

# for dict in json:
#     for key in dict:
#         for number in key:
#             print(number, end = " ")
#     print()


json = [
    {'1': 1, '2': 2, '3': 3}, 
    {'4': 4, '5': 5, '6': 6}, 
    {'7': 7, '8': 8, '9': 9},  
]
for item in json['data']:
    for key, value in item.items():
        print(f'{key}:{value}')

    for key in item:
        print(f'{key}:{item[key]}')

    print()


