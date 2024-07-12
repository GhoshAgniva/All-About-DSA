#Write a code to have the occarences of a  word
str=input().lower()
words = str.split(" ")
search=input("enter the input to be search:")
dict1={}
for char in words:
    if char in dict1:
        dict1[char]+=1
    else:
        dict1[char]=1
for i in dict1:
    if search == i:
        print(f"number of the occerence of the {search} word is {dict1[i]}")
        break
