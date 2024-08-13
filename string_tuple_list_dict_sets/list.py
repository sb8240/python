marks = [3, 5, 6, "Harry", True, 6, 7 , 2, 32, 345, 23]

print(marks[-3]) # Negative index
print(marks[len(marks)-3]) # Positive index
print(marks[5-3]) # Positive index
print(marks[2]) # Positive index
print(len(marks))
if "6" in marks:
  print("Yes")
else:
  print("No")

# # Same thing applies for strings as well!
if "Ha" in "Harry":
  print("Yes")

print(marks[0:7])
print(marks[1:9])
print(marks[1:9:3])

lst = [i*i for i in range(10)]
print(lst)
lst = [i*i for i in range(10) if i%2==0]
print(lst)

# # list methods

l=[1,2,3,4,4,5]

# l = [11, 45, 1, 2, 4, 6, 1, 1]
print(l)
l.append(7)
l.sort(reverse=True) # it sort the origianl list in descending oder
l.reverse() # it just reverse the original list 
print(l.index(1))
print(l.count(1))
m = l.copy()
m[0] = 0
l.insert(1, 899)
print(l)
m = [900, 1000, 1100]
k = l + m
print(k)
l.extend(m) # it will add list m at the end of list l
print(l)