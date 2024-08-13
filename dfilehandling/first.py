# with open ("hello.txt",'a+') as f:
#     f.write("hello python!")

# with open ('dfilehandling\hello.txt','r') as h:
#     a=h.read()
#     print(a)

# with open('dfilehandling\secoundfile.txt','x') as x:
#     print('done')

# with open ('dfilehandling\secoundfile.txt','a') as a: # a is append mode it is used to both read and write files.
#     a.writelines('hi my name is python 3.0, i am here to automate your boring stuff!')

# with open ("dfilehandling\secoundfile.txt",'w') as r:
#     r.writelines('omg! you got it, here i am python your companion, hello foks!, great work!')
#     print('done writing')
# # The only difference between the write() and writelines() is that write() is used to write a string to an already opened file while writelines() method is used to write a list of strings in an opened file.

# with open ("dfilehandling\hello.txt",'r') as r:
#     print(r.readlines()) # print all the lines in the form of list

# with open ("dfilehandling\hello.txt",'r') as r:
#     print(r.read()) # print the whole text if the form of string

# with open ("dfilehandling\hello.txt",'r') as r:
#     print(r.readline()) # print only the first line, it is made to read the content line by line

# with open ("dfilehandling\hello.txt",'r') as r:
#     print(r.readable()) # print wheather the content is readable or not(True/False)

# with open ('dfilehandling\marks.txt','r') as f:
#     i=0
#     while True:
#         i=i+1
#         line = f.readline()
#         if not line:
#             break
#         m1=line.split('/')[0]
#         m2=line.split('/')[1]
#         m3=int(line.split('/')[2])
# # for different subjects 
#         print(f'the marks of roll {i} student is:{int(m1)*2}')
#         print(f'the marks of roll {i} student is:{m2*2}')
#         print(f'the marks of roll {i} student is:{m3*2}')

# # r+ Opens a file for both reading and writing. 
# # The file pointer placed at the beginning of the file. 
# # w+ Opens a file for both writing and reading. Overwrites the existing file if the file exists.