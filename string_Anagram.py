str1=input("Enter the first String: ").lower()
str2=input("Enter the Second String: ").lower()

dict1={}
dict2={}

for char in str1:
    if char in dict1:
        dict1[char]+=1
    else:
        dict1[char]=1
for char in str2:
    if char in dict2:
        dict2[char]+=1
    else:
        dict2[char]=1


if dict1 == dict2:
    print("It is Anagram")
else:
    print("Not Anagram")

#Anather Approach
s1=input().lower()
s2=input().lower()
arr1=[]
arr2=[]
for i in s1:
    arr1.append(i)
for i in s2:
    arr2.append(i)
arr1.sort()
arr2.sort()
if arr1==arr2:
    print("its anagram")
else:
    print("not anagram")