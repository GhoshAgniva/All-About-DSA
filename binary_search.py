def binary_search(list,key):
    low=0
    high=len(list)-1
    while(low<=high):
        mid=high+low//2
        if list[mid]==key:
            return mid
        elif key>list[mid]:
            low=mid+1
        else:
            high=mid-1
<<<<<<< HEAD
        print(mid)
=======
>>>>>>> d066fa6c03f87287b195efd57b15aff2b94476c4
    return -1
n=int(input("Enter the size of the list: "))
list=[]
for i in range(n):
    elements=int(input("Enter the  element of list: "))
    list.append(elements)
print(list)
key=int(input("enter the element you want to seacrh:  "))

index=binary_search(list,key)
print("your element is on ",index)