print("hello myself")
print(5)

#comments in python is written like this.

#escape sequence charecters.
print("python newline\n charecter ")
print("backslash doublequote \"chrecter\" is also a newline charecter.")
print("hey,6,7",6,7)
#seperator
print("my ","name"," is by eminem.",sep="0",end="xxx")

#datatype.
#variables.: a container that holdes data
a=1
b=complex(23,67)#complesx nums.
print(a)
print("the type of a is ", type(a))
print(b)

#strings are immutable
#list is mutable
#tuple is immutable
#dictionary is mutable --->mapped data
#everything is object in python 

# #floor division operator -->//
# # modulus operator-->%--> remainder
# #power-->**

# #calculator

a=int(input("enter a number:"))
b=int(input("enter another number:"))

print("what you want to do?")
print("for addition press:c")
print("for substraction press:d")
print("for remainder press:e")
print("for multiplication press:f")
print("for power press:g")
print("for floor division press:h")


x=input("what you want to do?")
if x=="c":
    print(a+b)
elif x=="d":
    print(a-b)

#and so on...

#typecating: implicit,explicit
a="1"
b="2"
print(a+b)
#output: 12
print(int(a)+int(b))
#output: 3
c=5.5
d=7
print(c+d)
#output:12.5

# #input()-->function ---> takes as string
# #''' this can be used to write multiple line string
# #string is like an array of charecters.
a="my name is eminem"
for i in a:
    print(i)

