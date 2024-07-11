#write a program to merge two desending sorted array in a assending sorted manner

def merge_sort(l1,l2):
    res=[]
    i=len(l1)-1
    j=len(l2)-1
    while(j>=0 and i>=0):
        if l1[i]<l2[j]:
            res.append(l1[i])
            i=i-1
        else:
            res.append(l2[j])
            j=j-1
    while(i>=0):
        res.append(l1[i])
        i=i-1
    while(j>=0):
        res.append(l2[j])
        j=j-1
    return res
l1=[90,80,70,60]
l2=[10,9,8,7]
result=merge_sort(l1,l2)
print(result)