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

