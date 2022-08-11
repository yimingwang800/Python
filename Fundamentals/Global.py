a = 17

def func():
    global a    # Declare this a is global varible!
    a = 23      
    print(2, a)

print(1, a)
func()
print(3, a)