direction = 5
if not direction:
    pass
elif (direction % 2):
    turn = "left"
elif not (direction % 2):
    turn = "right"

print(turn)

#Not proper way
# direction = 5
# if (direction % 2):
#     turn = "left"
# elif not (direction % 2):
#     turn = "right"
# elif not direction:
#     pass

# print(turn)
