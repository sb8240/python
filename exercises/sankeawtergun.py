import random as r
l=[0,1,2] # snake, water, gun
# by using if-elif statements
score_comp= 0
score_user=0
print("\t\t\tWELCOME TO ROCK-PAPER-SCISSOR! ")
b = int(input("\nenter how many times you want to continue the game... : "))
for i in range(b):
    print("\n\t\t\tfor rock press 0\n\t\t\tfor paper press 1\n\t\t\tfor scissor press 2 ")
    c = r.choice(l)
    n = int(input("\t\t\tENTER A NUMBER : "))

    if n<0 or n>2:
        print("error!!!, please enter a number between 0-2")
    elif c == n:
        print("the computer has chosen", c)
        print("THE GAME HAS DRAWN!!!")
    elif c == n+1:
        print("the computer has chosen", c)
        print("The computer has won the game!!!")
        score_comp+=1
    elif c == n-2:
        print("the computer has chosen", c)
        print("Computer has won the game!!!")
        score_comp+=1
    elif c!=n or c!=n+1 or c!=n-2:
        print("the computer has chosen", c)
        print("you have won the game!!!")
        score_user+=1

    else:
        raise Exception("enter a number between 0-2")
print(f"scores: computer = {score_comp}, you = {score_user}")

# import random

# def check(comp, user):
#   if comp ==user:
#     return 0
    
#   if(comp == 0 and user ==1):
#     return -1
    
#   if(comp == 1 and user ==2):
#     return -1
    
#   if(comp == 2 and user == 0):
#     return -1

#   return 1
    
  
# comp = random.randint(0, 2)
# user = int(input("0 for Snake, 1 for water and 2 for Gun:\n"))

# score = check(comp, user)

# print("You: ", user)
# print("Computer: ", comp)

# if(score == 0):
#   print("Its a draw")
# elif (score == -1):
#   print("You Lose")
# else:
#   print("You Won")