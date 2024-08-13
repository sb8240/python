# tup0=(1,)
# print(tup0)
# tup1=(2,4,'string',67,53,'hello')
# print(tup1[3])
# if 4 in tup1:
#     print('yees')

# tup2=tup1[1:3]
# print(tup2)
# print(len(tup1))

# #tuples and strings are immutable.

# # tuple methods

colors=("Red","Blue","Black","Yellow","Pink")
print(type(colors))

t_list=list(colors)
print(type(t_list))

t_list.append("White")
print(t_list)

t_list.insert(2,"Brown")
print(t_list)

t_list[4]="Cyan"
print(t_list)

colors=tuple(t_list)
print(type(colors))
print(colors)

# Now lets try tuple methods (Only 2)
# 1 is index() and number 2 is count() method

marks=(19,18,10,12,18,16,15,16,19,14,16)
print(marks.count(16))
print(marks.count(19))
print(marks.count(10))

print()

print(marks.index(10))
print(marks.index(16))
print(marks.index(14))
print(marks.index(19))
print(marks.index(15))
print(marks.index(16,1,6)) # # 16 is in 5th index between 1 to 6



