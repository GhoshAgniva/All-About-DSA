#write a program to print all even number from 1 to n
n=int(input("Enter your number: "))
for i in range(1,n+1):
    if i%2==0:
        print(i)