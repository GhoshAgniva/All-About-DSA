<<<<<<< HEAD
#Taking user input as list format
n=int(input("Enter the size of the list: "))
l=[]
for i in range(n):
    elements=int(input("Enter the  element of list: "))
    l.append(elements)
print(l)

#print those element whose are even in nature
l=[1,23,44,67,88,12]
for i in range(len(l)):
    data=l[i]
    if data%2==0:
        print(data)

#I want to print the Index of the even number

l=[1,23,44,67,88,12]
for i in range(len(l)):
    data=l[i]
    if i%2==0:
        print(i)



#Finiding avarage of a given list elements

l=[1,23,44,67,88,12]
sum=0
for i in range(len(l)):
    data=l[i]
    sum=sum+data
avg=sum/len(l)
print(avg)




#finiding the maximum value in a list
l=[-1,-23,-44,-67,-88,-12,-99]
max=l[0]
for i in range(len(l)):
    data=l[i]
    if data > max:
        max=data
print(max)

# -------------------------------------------------------------------------------------------
##finiding the Second maximum value in a list
l=[-1,-23,-44,-67,-88,-12,-99]
max=l[0]
for i in range(len(l)):
    data=l[i]
    if data > max:
        max=data

#create a new list without the maximum element
new_list=[]
for i in l:
    if i != max:
        new_list.append(i)
#extracting the second biggest element from the list
max1=new_list[0]
for i in range(len(new_list)):
    if data>max1:
        max1=data
print(max1)


##Anather methode for finiding the Second maximum value in a list

#assume which is max1 and max2
l=[11,2,3,44,55,678,678,-2]
if l[0]>l[1]:
    max1=l[0]
    max2=l[1]
else:
    max2 = l[0]
    max1 = l[1]

#finding the second max value
for i in range(2,len(l)):
    if l[i]>max1:
        max2=max1
        max1=l[i]
    elif l[i]>max2:
        max2=l[i]
print(max2)





=======
#what is the output for this code
def print_num(num):
    if num==0:
        print(num)
        return
    print_num(num-1)
    print(num)
num = 5
res=print_num(num)
print(res)
>>>>>>> d066fa6c03f87287b195efd57b15aff2b94476c4
