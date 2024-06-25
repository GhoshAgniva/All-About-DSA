#Normal Approach
num=int(input())
res=[]
for i in range (1,num):
    if num%i==0:
        res.append(i)

if sum(res)==num:
    print("perfect Number")

else:
    print("not perfect")




#functional Approach
def check_perfect(num):
    sum=0
    for i in range(1,num):
        if num%i==0:
            sum=sum+i
    return sum
num=int(input("enter the number: "))
res=check_perfect(num)
if res==num:
    print("it is a perfect number")
else:
    print("it is not perfect")





#Adding all the perfect number from 1 to 10000

def check_perfect(num):
    sum=0
    for i in range(1,num):
        if num%i==0:
            sum=sum+i
    return sum
for k in range(1,10000):
    num=k
    res=check_perfect(num)
    if res==num:
        print(num)

