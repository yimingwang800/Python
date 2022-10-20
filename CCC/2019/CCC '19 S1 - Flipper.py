input_instruction = input()
grid = [[1,2],[3,4]]
grid_vertical = [[0,0],[0,0]]
grid_horizontal = [[0,0],[0,0]]
for x in range (len(input_instruction)):
    if (input_instruction[x] == 'V'):
        for i in range(2):
            for j in range(2):
                grid_vertical[i][j] = grid[i][1-j] 
        for i in range(2):
            for j in range(2):
                grid[i][j] = grid_vertical[i][j]
    elif (input_instruction[x] == 'H'):
        for i in range(2):
            for j in range(2):
                grid_horizontal[i][j] = grid[1-i][j] 
        for i in range(2):
            for j in range(2):
                grid[i][j] = grid_horizontal[i][j]

for i in grid:
    for j in i:
        print(j,end=" ")
    print()