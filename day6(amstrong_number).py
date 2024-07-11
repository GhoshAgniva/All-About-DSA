


# #Methode 2: Functional approach (without using string)

def count_digit(num):
    count=0
    while num!=0:
        num=num//10
        count=count+1
    return count
def amstrong(num):
    digit=count_digit(num)
    res=0
    while num!=0:
        rem=num%10
        res=(rem**digit)+res
        num=num//10
    return res
num=int(input("Enter Your number: "))
res=amstrong(num)
if num==res:
    print("it is a amstrong number")
else:
    print("it is not a amstrong number")



#printing all the amstrong number from 1 to 10000
def count_digit(num):
    count=0
    while num!=0:
        num=num//10
        count=count+1
    return count
def amstrong(num):
    digit=count_digit(num)
    res=0
    while num!=0:
        rem=num%10
        res=(rem**digit)+res
        num=num//10
    return res
for k in range(1,10000+1):
    num=k
    res=amstrong(num)
    if num==res:
        print(num)




#Anather methode
# num=153
# i=num
# sum=0
# while i>0:
#     sum=sum+(i%10)**3
#     i=i//10
# print(num==sum)