# for i in range(0,6): # lazy caterer’s sequence
#     print(int(((i*i)+i+2)/2),end=' ')

# tuple=(1,2,3,4,5,6,7)
# list=[1,2,3,4,5,6,7]
# it=int(input("press list =1 or tuple =2: "))
# n=int(input('enter a no. you want to find: '))

# def linear_search(it,n):
#     found=True
#     for i in range(len(it)):
#         if it[i]==n:
#             found=False
#             print(type(it),f'the no. is found, its in {i} position.')
#             break
#         elif not found:
#             print('your element is not in the list.')

# if it==1:
#     it=list[:]
# if it==2:
#     it=tuple()
# linear_search(it,n)

# list=[34,56,1,2,12,89,19,5]
# list.sort()
# print(list)


# file=open('a_new_file.txt','r+')
# file.write('hello my name is python')
# file.seek(0)
# x=file.read()
# print(x)
# file.close

# import shutil
# shutil.copyfile('a_new_file.txt','a_new_file2.txt')

# dict={}
# with open('dictionary.txt') as d:
#     a=d.readline()#for line in f:
#     (key,val)=a.split()
#     d[int(key)]=val
    
# print(d)

# with open('dictionary.txt','r') as f:
#     for line in f:
#         print(line)

import csv
fields=[]
rows=[]
with open('student_database.csv','r') as file:
    #creating a csv reader object
    reader=csv.reader(file)
    #extracting field names through first row
    fields=next(reader) #csvreader is an iterable object. Hence, .next() method returns the current row and advances the iterator to the next row. 
    for row in reader:
        rows.append(row)
    
    print('total no. of rows: %d'%(reader.line_num))
#printing first 2 rows
print('\n first 2 rows are:\n')

#printing the field names
print('field names are:\n'+','.join(field for field in fields))


for row in rows[:2]:
    for col in row:
        print(col,end=' '),
    print('\n')



