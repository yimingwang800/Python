def empty_function():
    pass    # pass means doing nothing!
def my_function():
    print("Hello from a function")
def my_function_1(first_str, second_str):
    print(first_str + " " + second_str)
def child_function(child_1, child_2, child_3="Midorya"):
    print("The third child is " + child_3)
def return_function(x):
    return 5*x

y = return_function(x=3)
print (y)
print(return_function(x=5))

child_function(child_2="Bakugo", child_1="Shoto")
child_function(child_1="Shoto", child_2="Bakugo", child_3="Eri")

my_function_1("Cool and", "Awesome")

empty_function()
my_function()