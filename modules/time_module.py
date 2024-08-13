import time
timestamp = time.strftime('%H:%M:%S')
hourshand = int(time.strftime('%H'))
minuteshand = int(time.strftime('%M'))
secondshand = int(time.strftime('%S'))
print(timestamp)

# 06:00:00 to 11:59:59 - Morning
# 12:00:00 to 16:59:59 - Afternoon
# 17:00:00 to 21:59:59 - Evening
# 22:00:00 to 05:59:59 - Night

if hourshand in range (5,12) and minuteshand <=59 and secondshand<=59:
  print("Good Morning Sir !")
elif hourshand in range (13,18) and minuteshand <=59 and secondshand<=59:
  print("Good Afternoon Sir !")
elif hourshand in range (18,24) and minuteshand <=59 and secondshand<=59:
  print("Good Evening Sir !")
else:
  print("Good Night Sir !")

# # alternate

t = time.strftime('%H:%M:%S') 
hour = int(time.strftime('%H'))
# hour = int(input("Enter hour: "))
# print(hour)

if(hour>=0 and hour<12):
  print("Good Morning Sir!")
elif(hour>=12 and hour<17):
  print("Good Afternoon Sir!")
elif(hour>=17 and hour<0):
  print("Good Night Sir!")


# def usingWhile():
#   i = 0
#   while i<50000:
#     i = i +1
#     print(i) 

# def usingFor():
#   for i in range(50000):
#     print(i)

# init = time.time()
# usingFor()
# t1 = time.time() - init
# init = time.time()
# usingWhile()
# print(time.time() - init)
# print(t1)


# print(4)
# time.sleep(3)
# print("This is printed after 3 seconds")
 
t = time.localtime()
formatted_time = time.strftime("%Y-%m-%d %H:%M:%S", t)

print(formatted_time) 