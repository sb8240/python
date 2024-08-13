# # Decorators modifies a function
# # *args --> method of taking all the arguments as tuple 
# # **kwargs --> method of taking all the arguments as dictioary

def greet(fx):
  def mfx(*args, **kwargs):
    print("Good Morning") #1
    fx(*args, **kwargs)
    print("Thanks for using this function") #3
  return mfx

@greet # decorator
def hello():
  print("Hello world") #2

@greet
def add(a, b):
  print(a+b)
  
# greet(hello)()
# hello()
# greet(add)(1, 2)
add(1, 2)