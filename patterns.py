#here we are going to prctice printing different types of patterns

# #PYRAMID

# a=int(input("enter the number of rows:"))
# for r in range(a+1):
#     for c in range(r):
#         print('*',end='')
#     print('')

# b=int(input("enter the number of rows :"))
# for r in range(b+1):
#     for c in range(1,r+1):
#         print(c,end='')
#     print('')

# x=int(input("enter the number pf rows:"))
# for r in range(x+1):
#     for c in range(1,r+1):
#         print(c,end=' ')
#     print('')

# #INVERTED PYRAMID

# rows=int(input("enter the number of rows:"))
# b = 0
# # reverse for loop from 5 to 0
# for i in range(rows, 0, -1):
#     b += 1
#     for j in range(1, i + 1):
#         print(b, end=' ')
#     print('\r') # # Carriage return or \r is a very unique feature of Python. \r will just work as you have shifted your cursor to the beginning of the string or line.

# rows=int(input("enter the number of rows:"))
# # reverse for loop from 5 to 0
# for i in range(rows, 0, -1):
#     for j in range(1, i + 1):
#         print(rows, end=' ')
#     print('\r')

# rows=int(input("enter the number of rows:"))
# # reverse for loop from 5 to 0
# for i in range(rows, 0, -1):
#     for j in range(1, i + 1):
#         print(j, end=' ')
#     print('\r')

# rows=int(input("enter the number of rows:"))
# # reverse for loop from 5 to 0
# for i in range(rows, 0, -1):
#     for j in range(1, i + 1):
#         print('*', end=' ')
#     print('\r')

# b=int(input("enter the number of rows :"))
# for r in range(1,b+1,2):
#     for c in range(1,r+1):
#         print(r,end=' ')
#     print('')
# #=======================================================
# a=int(input())
# for k in range(0,a+1):
#     for l in range(1,k+1):
#         print(l,end='')
#     print(' ')
# #=======================================================

# count=0
# x=int(input())
# for i in range(x,0,-1):
#     count+=1
#     for j in range(1,i+1):
#         print(count,end=' ')
#     print('\r')
# print()
# count=-1
# x=int(input())
# for i in range(x,0,-1):
#     count+=1
#     for j in range(1,i+1):
#         print(count+j,end=' ')
#     print('\r')

# # LEFT SIDE TRIANGLE
# a=int(input('enter a no.: '))
# for i in range(a+1):
#     for j in range(i):
#         print("*",end=' ')
#     print(' ')
# for i in range(a-1, 0, -1):
#     for j in range(1, i + 1):
#         print("*", end=' ')
#     print(' ')

# #CENTERED TRIANGLE

# def triangle(n):

#     k=n-1 #no. of spaces

#     for i in range(n): #no. of rows
#         for j in range(k): #no. of spaces in each row
#             print(end=' ')
#         k=k-1 #decreasing no. of spaces in each row
        
#         for j in range(i+1): #no. of columns
#             print("* ",end='') 
#         print("\r") #for new line

# n=int(input("enter a no. : "))
# triangle(n)

# n=int(input("enter a no. : "))
# for i in range (n):
#     if i==0:
#         print(f'the sum of {i} + {i} =', 0)
#     else:
#         print(f'the sum of {i} + {i-1} =', i+(i-1))

# name=input('enter a name: ')

# for i in range(len(name)):
#     if i%2==0:
#         print(name[i])

# n=input("enter name: ")
# x=int(input('enter a number: '))
# print(n[x:])

# # Write a Program to extract each digit from an integer in the reverse order.
# n=(int(input('enter: ')))
# rev=0
# while n>0:
#     rev=(rev*10)+n%10
#     n=n//10
# print(rev)

# #pascal triangle

# def solve(n):
#     for i in range(1, n+1):
#         # for j in range(0, n-i+1):
#         #     print(' ', end='')
    
#         # first element is always 1
#         C = 1
#         for j in range(1, i+1):
    
#             # first value in a line is always 1
#             print(' ', C, sep='', end='')
    
#             # using Binomial Coefficient
#             C = C * (i - j) // j
#         print()

# n = int(input('enter a no. : '))
# solve(n)


# k=3 #no. of spaces
# for i in range(4): #no. of rows
#     for j in range(k): #no. of spaces
#         print(end=' ')
#     k=k-1 #decreasing no. of spaces
#     for j in range(i+1): #no. of column
#         print("*",end=' ')
#     print("\r") #for new line
# for l in range(2):
#     print("  | |")



    
