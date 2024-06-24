import math
#write a program that print all the factors of a number[O(n)]
num=int(input("enter the number: "))
for i in range(1,num+1):
    if num%i==0:
        print(i)

#write the same code with less time complexcity[O(n/2)]

num=int(input("enter the number: "))
for i in range(1,num+1//2):
    if num%i==0:
        print(i)
print(num)

#write the same code using less complexcity [O(root(n)]
num=int(input("enter the number: "))
for i in range(1,int(math.sqrt(num))+1):
    if num%i==0:
        print(i)
        print(num//i)
#write the same code using less complexcity with sorted element [O(root(n)]
num=int(input("enter the number: "))
for i in range(1,int(math.sqrt(num))+1):
    if num%i==0:
        print(i)
for i in range(int(math.sqrt(num)),0,-1):
    if num%i==0:
        print(num//i)



