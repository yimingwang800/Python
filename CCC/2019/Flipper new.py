grid = [[1,2],[3,4]]
input_instruction = input()
Total_V = 0
Total_H = 0
for x in range (len(input_instruction)):
    if (input_instruction[x] == 'V'):
        Total_V += 1
    if (input_instruction[x] == 'H'):
        Total_H += 1

if (Total_V % 2):
    grid[0][0], grid[0][1] = grid[0][1], grid[0][0]
    grid[1][0], grid[1][1] = grid[1][1], grid[1][0]
if (Total_H % 2):
    grid[0][0], grid[1][0] = grid[1][0], grid[0][0]
    grid[0][1], grid[1][1] = grid[1][1], grid[0][1]

for i in grid:
    for j in i:
        print(j,end=" ")
    print()
