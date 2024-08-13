def calculategmean(a,b): #a fuction for calculating geometric mean
    mean=(a*b)/(a+b)
    print(mean)


a=int(input("enter a number:"))
b=int(input("enter another number:"))
calculategmean(a,b) #function call

def greaterno(x,y):
    if x>y:
        print(x, "is greater than", y)
    elif x==y:
        print(x, "is equal to", y)
    else:
        print(y, "is greater than", x)

x=int(input("enter a number:"))
y=int(input("enter another number:"))

greaterno(x,y)

#default argument
#keyword argument
#required argument

#variable - length argument

def avg(*nums):
    #print(type(nums)) <-- tuple
    sum=0
    for i in nums:
        sum=sum+i
    return sum/len(nums) #return is used to return the value of expression back to calling function.

a=avg(1,2,3,4,5,6)
print(a)




