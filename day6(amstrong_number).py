# #Methode 1: Funtional approach(using string concatination)
def check_amstrong(num):
    sum=0
    for i in num:
        p=(int(i)**3)
        sum=sum+p
    return sum
num=input("enter the number: ")
result=check_amstrong(num)
if int(num)==result:

    print("it is a amstrong number")
else:
    print("it is not a amstrong number")


# #Methode 2: Functional approach (without using string)
# def check_amstrong(num):
#     count=0
#     sum=0
#     while(num!=0):
#         num=num//10
#         count+=1
#         rem=num%10
#         sum=rem**count+sum
#         return sum   ###changes neded
# num=1634
# countt=check_amstrong(num)
# print(countt)


#Anather methode
# num=153
# i=num
# sum=0
# while i>0:
#     sum=sum+(i%10)**3
#     i=i//10
# print(num==sum)