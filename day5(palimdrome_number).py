#functional Approach:reduce 1 temporary varriable

def reverse(num):
    res = 0
    while (num != 0):
        rem = num % 10
        res = (res * 10) + rem
        num = num // 10
    return res
num=int(input("enter your number: "))
res=reverse(num)
if num==res:
    print("its a palimdrome number")
else:
    print("it is not a palimdrome number")


#printing all the palimdrome from 1 to 10000

def reverse(num):
    res = 0
    while (num != 0):
        rem = num % 10
        res = (res * 10) + rem
        num = num // 10
    return res
for k in range(1,10000):
    num=k
    res=reverse(num)
    if num==res:
        print(num)


#Write a program that print a triangle made by palimdrome number till 121
def reverse(num):
    res = 0
    while (num != 0):
        rem = num % 10
        res = (res * 10) + rem
        num = num // 10
    return res

num=121
rows=int(input("Enter The number of rows: "))
k=1
for i in range(1,rows+1):
    for j in range(i):
        while True:
            if reverse(k)==k:
                print(k,end=" ")
                k=k+1
                break
            else:
                k=k+1
    print()