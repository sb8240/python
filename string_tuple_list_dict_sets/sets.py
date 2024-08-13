# # sets are unordered collection of data items. sets are unchangeable
# # it doesnot contain duplicate items.
# # it doesnt follow oder

# s={1,2,3,4,5,5,3,4,44,4,4}
# print(s)

# name={'souro',True,True,False,65,78,89}
# print(name)

# # empty set

# s=set()
# print(type(s))

# # methods of sets

# s = {12,23,34,34,45,5,12,"Joy","a",12.3}

# for i in s:
#   print(i)

# print("s: ",end = '')
# s.add("last")  # add data
# print(s)

# s.discard(12) # Remove Element but if element is not present in set not throw error
# print(s)

# s.remove(45) # Remove element . if element is not present Throw error
# print(s)

# s.update('6')
# print(s)

# s3 = s.copy() # copy set
# print(s3)

# s.clear() # clear()
# print(s)




# # #Union , Intersection, isdisjoint superset, subset

# s1 = {12,3,4,45,6,89}
# s2 = {23,34,7,8,45}
# s3 = {12,3,4}
# s4 = {12,2,4}

# uni = s1.union(s2)
# print("Union: ",uni)

# inter = s1.intersection(s2) #or inter = s1 & s3
# print("Intersection: ",inter)

# super_set = s1.issuperset(s3)
# print("Super set: ",super_set)

# subset = s3.issubset(s1)
# print("Subset",subset)

# # if two set have no common elements
# disjoint = s2.isdisjoint(s3)
# print(disjoint)

# symm = s3.symmetric_difference(s4)
# print(symm)

# # ------ pop, del ------
# s2 = {23,34,7,8,45}
# p = s2.pop()  # random element delete
# print(s2)
# print(p)
# # del s2
# # print(s2)

# # check items
# items = {"a","sd","sded","efas"}

# if "sd" in items:
#     print("present")
# else:
#   print("Not present")
