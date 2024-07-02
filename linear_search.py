#write a program that perform linear search
def liniar_search(arr,key):
    for i in range(0,len(arr)):
        if arr[i]==key:
            return i
    return -1
n=int(input("Enter the size of the list: "))
arr=[]
for i in range(n):
    elements=int(input("Enter the  element of list: "))
    arr.append(elements)
print(arr)
key=int(input("enter the element you want to seacrh:  "))

index=liniar_search(arr,key)
print("your element is on ",index)
