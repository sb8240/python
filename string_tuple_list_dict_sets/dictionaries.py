# # dictionary is a key value pair sepreted by commas

# dict={1:'name1',2:'name2',3:'name3',4:'name4'} # dict={'name1':1,'name2':2}
# print(dict[2]) # this will throw an error
# print(dict.get(2)) # this will not throw an error #print(dict.get('name1))
# print(dict.keys())
# print(dict.values())

# for key in dict.keys():
#     print(key)

# # ====================================
# for values in dict.values():
#     print(values)

# for value in dict.keys():
#     print(dict[value])
# # ====================================

# for key in dict.keys():
#     print(f"The value corresponding to the key {key} is {dict[key]}")

# print(dict.items())

# for key,value in dict.items():
#     print(f"The value corresponding to {key} is {value}")

# ep1 = {122: 45, 123: 89, 567: 69, 670: 69}
# ep2 = {222: 67, 566: 90}

# ep1.update(ep2) # will merge both dicts.
# ep1.clear() # will clear the whole dict.
# ep1.pop(122) # will del the specified key value pair
# ep1.popitem() # del one key-value pair from last.
# del ep1[122] # will del the specified key value pair
# print(ep1)
# ep1.popitem()
# print(ep1)

# d={1:'a',2:'b'}
# d.update({3:'c'})
# print(d)
