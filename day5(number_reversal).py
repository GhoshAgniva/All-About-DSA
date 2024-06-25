
#write a program to reverse a number without using string concept
num=int(input("Enter the number: "))
res=0
while(num!=0):
    rem=num%10
    res=(res*10)+rem
    num=num//10
print(res)