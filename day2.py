#write a program to merge two sorted array
def merge_sort(l1,l2):
    res=[]
    i=0
    j=0
    while(j<len(l2) and i<len(l1)):
        if l1[i]<l2[j]:
            res.append(l1[i])
            i=i+1
        else:
            res.append(l2[j])
            j=j+1
    while(i<len(l1)):
        res.append(l1[i])
        i=i+1
    while(j<len(l2)):
        res.append(l2[j])
        j=j+1
    return res
l1=[1,2,3,4,5]
l2=[6,10]
result=merge_sort(l1,l2)
print(result)