
def is_perefect_cube(n):
    if n>=0:
        sr = int(n**(1/3)) 
        return ((sr*sr*sr)==n)
    return False

n=int(input('enter a no. : '))
if (is_perefect_cube(n)):
    print('yess')
else:
    print('no')

# Program to check if a number is prime or not

# define a flag variable
# flag = False
# num=int(input('enter a number: '))
# if num == 1:
#     print(num, "is not a prime number")
# elif num > 1:
#     # check for factors
#     for i in range(2, num):
#         if (num % i) == 0:
#             # if factor is found, set flag to True
#             flag = True
#             # break out of loop
#             break

#     # check if flag is True
#     if flag:
#         print(num, "is not a prime number")
#     else:
#         print(num, "is a prime number")

# def is_prime(n):
#     if n <= 1:
#         return False
#     for i in range(2, int(n**0.5) + 1):
#         if n % i == 0:
#             return False
#     return True

# def factorial(n):
#     result = 1
#     for i in range(1, n + 1):
#         result *= i
#     return result

# def main():
#     n = int(input("Enter a number: "))
#     primes = [x for x in range(2, n + 1) if is_prime(x)]
#     factorials = [factorial(x) for x in primes]

#     with open("factorials.txt", "w") as f:
#         for i in range(len(primes)):
#             f.write(f"{primes[i]}! = {factorials[i]}\n")

# if __name__ == "__main__":
#     main()

# with open('factorials.txt','r') as f:
#     a =f.read()
#     with open('copy_factorials.txt','a') as cf:
#         cf.write(a)

# def fibonacci(n):
#     result = [0, 1]
#     while len(result) < n:
#         result.append(result[-1] + result[-2])
#     return result

# def factorial(n):
#     result = 1
#     for i in range(1, n + 1):
#         result *= i
#     return result

# def main():
#     n = int(input("Enter number of terms: "))
#     print("Fibonacci sequence:", fibonacci(n))
#     print(f"Factorial of {n}:", factorial(n))

# if __name__ == "__main__":
#     main()


# def factorial(n):
#     result = 1
#     for i in range(1, n + 1):
#         result *= i
#     return result

# def permutation(n, r):
#     return factorial(n) / factorial(n - r)

# def combination(n, r):
#     return factorial(n) / (factorial(r) * factorial(n - r))

# def main():
#     n = int(input("Enter value of n: "))
#     r = int(input("Enter value of r: "))

#     choice = input("Do you want permutation (p) or combination (c)? ")
#     if choice == "p":
#         result = permutation(n, r)
#     else:
#         result = combination(n, r)

#     print(f"{n} {choice} {r}: {result}")

# if __name__ == "__main__":
#     main()

# def count_vowels(filename):
#   vowels = "aeiouAEIOU"
#   with open(filename, "r") as file:
#     text = file.read()
#     count = 0
#     for char in text:
#       if char in vowels:
#         count += 1
#     return count

# filename = input("Enter the filename: ")
# vowel_count = count_vowels(filename)
# print("Number of vowels:", vowel_count)

# listt= [3,6,7,5,12,10,30,56,33,48,90]
# a=sorted(listt, reverse=True)
# print(a)



def series(n):
    s=1
    for i in range(n+1):
        s+=i
        print(s, end=' ')

a= int(input("enter upto how many terms you want the series:"))
series(a)
