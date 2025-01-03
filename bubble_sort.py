#write bubble sort in assending order
def bubble_sort(list1):
    for k in range(0,len(list1)-1):
        for i in range(0,len(list1)-1):
            if list1[i]>list1[i+1]:
                list1[i],list1[i+1]=list1[i+1],list1[i]
    return list1
list1=[8,143,420,6106,90,69,120,18]
result=bubble_sort(list1)
print(result)




#write the code in decending order
def bubble_sort(list1):
    for k in range(0,len(list1)-1):
        for i in range(0,len(list1)-1):
            if list1[i]<list1[i+1]:
                list1[i],list1[i+1]=list1[i+1],list1[i]
    return list1
list1=[8,143,420,6106,90,69,120,18]
result=bubble_sort(list1)
print(result)
