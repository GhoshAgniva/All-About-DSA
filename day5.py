#Anather functional approach to get the prime number

def check_prime(num):
    if num <= 1:
        print("False input")
    for i in range(2,num):
        if (num%i==0):
            return False
    return True

num=int(input("Enter your number: "))
res=check_prime(num)
if res==True:
    print("its a prime number")
else:
    print("its not a prime number")

#Anather functional approach to get the prime number with less time complexcity
def check_prime(num):
    if num <= 1:
        print("False input")
    for i in range(2,num//2):
        if (num%i==0):
            return False
    return True

num=int(input("Enter your number: "))
res=check_prime(num)
if res==True:
    print("its a prime number")
else:
    print("its not a prime number")