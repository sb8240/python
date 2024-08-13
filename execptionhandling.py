# a=input("enter a number: ")
# print(f"Multiplication table of {a} is: ")
# try:
#     for i in range(1,11):
#         print(f"{int(a)} X {i}={int(a)*i}")

# except Exception as e:
#     print(e)

# # or execpt:
# #        print("invalid input!")

# print("code is running")

# def func():
#     try:
#         list=[5,6,7,3,8]
#         x=int(input("enter a index: "))
#         print(list[x])
#         return 1
#     except:
#         print("i am in except block")
#         return 0
#     finally:
#         print("i am in finally block an i will execute no matter what!")

#     print("i will not execute if try or execpt get executed")

# y=func()  
# print(y)  

# # raising custom error 

# a = int(input("Enter any value between 5 and 9"))

# if(a<5  or a>9):
#   raise  ValueError("Value should be between 5 and 9")

# a=input("enter the word: ")

# if str(a)=="QUIT":
#     print("good to go")
# else:
#     raise SyntaxError("you have to write (QUIT)")