# with open('sample.txt', 'w') as f:
#   f.write('Hello World3!')
#   f.truncate(3) # only 3 charecters will be added

# with open('sample.txt', 'r') as f:
#   print(f.read())

with open('dfilehandling\sample.txt','r') as f:
    f.seek(5)
    print(f.tell())
    print(f.read())
    print(f.tell())