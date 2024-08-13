names="name1,name2,name3"
print(len(names))
print(names[0:4])#this is same as names[:4]
print(names[1:6])
print(names[0:-5])#this is same as names[0:len(names)-5]
print(names[-6:-3])

#string manipulation.
a="nameofSomeone,$$$$$$$$"
print(a.upper())
print(a.lower())
print(a.rstrip("$"))
print(a.replace("NameofSomeone","eminem"))
print(a.split(","))
print(a.capitalize())#capitalize only first charecter and converts all other into lower case.
print(a.count("$"))
print(a.endswith("$"))#returns boolean datatype.
print(a.endswith("$",13,16))
print(a.find("S"))
print(a.index("S"))#if not found then it shows error.
print(a.isalnum())#alphanumeric a-z,0-9
print(a.isalpha())#a-z only
print(a.islower())#returns boolean value
print(a.isprintable())#returns boolean value
print(a.isspace())#returns boolean value
print(a.istitle())#returns boolean value
print(a.startswith("n"))
print(a.swapcase())#swaps upper-lower case.
print(a.title())

# # The format() method formats the specified value(s) and insert them inside the string's placeholder.

# # The placeholder is defined using curly brackets: {}. Read more about the placeholders in the Placeholder section below.

# # The format() method returns the formatted string.

# txt1 = "My name is {fname}, I'm {age}".format(fname = "John", age = 36)
# txt2 = "My name is {0}, I'm {1}".format("John",36)
# txt3 = "My name is {}, I'm {}".format("John",36) 

a = "hello this is python here!"
b = a.split()
print(b) # will return a list of string after splitting
c = "/".join(b) #  will join elements of list b by /
print(c)