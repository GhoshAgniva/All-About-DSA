

#write a program that print prime number 
#Methode1:Normal Approach
num=int(input())
for i in range(2,(num//2)+1):
    if num%i==0:
        print("it is not a prime number")
        break

    else:
        print("prime number")
        break

#Methode2: Function approach
def check_prime(num):
    count=0
    for i in range(1,num+1):
        if num%i==0:
            count+=1
    return count
num=int(input())
count=check_prime(num)
if count==2:
    print("its a prime number")
else:
    print("its not a prime ")


#write a code that print prime number from 0 to 10000

def check_prime(num):
    count=0
    for i in range(1,num+1):
        if num%i==0:
            count+=1
    return count
for k in range(1,10000+1):
    num=k
    count=check_prime(num)
    if count==2:
        print(num)

