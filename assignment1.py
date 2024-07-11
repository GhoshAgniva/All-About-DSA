#Given that an intiger N,returns the smallest intiger greater than N,
#the sum of those digits is twice as big as the sum of digits of N.
#examples:1. Given N =14, The function should return 19.
#the sum of the two digits of 19 is(1+9=10) is twice as big as sum of digits of 14(1+4=5)
#2.Given N=10,the function should return 11
#3.given N=99 , the function should return 9999

def add_digit(num):
    sum=0
    while num != 0:
        rem= num % 10
        sum= sum+rem
        num=num//10
    return sum
num=int(input("enter the number: "))
num1=num+1
while((add_digit(num)*2)!=add_digit(num1)):
    num1=num1+1
print(num)