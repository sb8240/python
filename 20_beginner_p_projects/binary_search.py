pos=0
steps=0
def binary_search(new_list,n):

    lower_bound = 0
    upper_bound = len(new_list)-1
    
    while lower_bound <= upper_bound:
        print("Step", globals()['steps'],":", str(new_list[lower_bound:upper_bound]))
        globals()['steps'] = globals()['steps']+1

        mid = (lower_bound+upper_bound)//2

        if list[mid]==n:
            globals()['pos'] = mid
            return True
        else:
            if list[mid] < n:
                lower_bound = mid+1
            else:
                upper_bound = mid-1
    return False

list = []
l = int(input("enter the number of elements you want to add in a list: "))
for i in range(l):
    element = int(input())
    list.append(element)
    
list.sort()
new_list = list

n = int(input("enter a number you want to search: "))
print(new_list)

if binary_search(new_list, n):
    print("Found at ", pos)
else:
    print("Not found!")
