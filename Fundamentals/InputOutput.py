var = input()
print(type(var))
print(type(int(var)))
print("Hello World!", "Again!\nAgain!")

x = "abc"
y = 7654321.7654321
# Format method 1
print("x is {}, y is {}".format(x, y))
# Format method 2
print("x is {: >8}, y is {:,.2f}".format(x, y))
# Format method 3
print(f"x is {x: >8}, y is {y:,.2f}")
