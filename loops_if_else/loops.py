# #if else statement.

a=int(input("enter your time in HH.MM format:"))

if a in range(5, 12):
    print("good morning")
elif a in range(12, 17):
    print("good noon")
else:
    print("good night")


#number in range() expression returns a boolean value: 
#True if number is present in the range(), 
# False if number is not present in the range.
range_1 = range(2, 20, 3)
number = int(input('Enter a number : '))
 
if number in range_1 :
    print(number, 'is present in the range.')
else :
    print(number, 'is not present in the range.')

x = int(input("Enter the value of x: ")) 
#it is same as switchcase in c++
#but here you dont have to use break after every cases to end it.
# x is the variable to match
match x:
    # if x is 0
    case 0:
        print("x is zero")
    # case with if-condition
    case 4:
        print("case is 4")
    case _ if x!=80:
        print(x, "is not 80")
    case _:
        print("last case")

count=int(input("enter a no:"))
while(count<6):
    print(count)
    count=count+1

#do while loop will iterate atleat 1 time regardless of the condition is true or false
#pyhton do not have any do while loop.

for i in range(12):
  if(i == 10):
    print("Skip the iteration")
    continue
  print("5 X", i, "=", 5 * i)
  
i = 0
while True:
  print(i)
  i = i + 1
  if(i%100 == 0):
    break

# continue statement skips to the next iteration.
# break statement breaks out of the loop.
# pass	Do nothing. Ignore the condition in which it occurred and proceed to run the program as usual

# # enumerate function

# # normal method
marks = [2,56,89,99,35,56]
# index=0
# for mark in marks:
#     print(mark)
#     if (index==4):
#         print("hello python")
#     index+=1
# # by using enumerate func.

for index, mark in enumerate(marks,start=2): # start changes the starting index no.
    print(mark)
    if index==4:
        print('hello python 3!')
