#printing even and odd number in different column
n=int(input("Enter your number: "))
for i in range(1,n+1):
    if i%2!=0:
        print(i,end=" ")
    else:
        print(i)