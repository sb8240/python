x=97 # global variable

def func():
    global x # changing local to global
    print("x is local",x)
    

print('x is global',x)
func()